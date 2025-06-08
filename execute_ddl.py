"""
세번째 실행되는 파일
clickhouse_ddl 디렉토리 하위의 모든 DDL 파일을 ClickHouse에 실행
"""

import os
import re
import time
import clickhouse_connect
from pathlib import Path
from typing import List, Dict


class ClickHouseDDLExecutor:
    """생성된 DDL 파일들을 ClickHouse에 실행하는 클래스"""

    def __init__(
        self, host="localhost", port=8124, username="clickhouse", password="clickhouse"
    ):
        """ClickHouse 연결 초기화"""
        self.client = clickhouse_connect.get_client(
            host=host, port=port, username=username, password=password
        )

    def parse_ddl_file(self, ddl_file_path: Path) -> Dict:
        """DDL 파일을 파싱하여 데이터베이스명과 개별 DDL 문들을 추출"""
        try:
            with open(ddl_file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(ddl_file_path, "r", encoding="latin-1") as f:
                content = f.read()

        result = {
            "file_path": ddl_file_path,
            "database_name": None,
            "create_database_stmt": None,
            "create_table_stmts": [],
            "errors": [],
        }

        try:
            # 데이터베이스 생성 문 추출
            db_pattern = r"CREATE DATABASE IF NOT EXISTS (\w+);"
            db_match = re.search(db_pattern, content)
            if db_match:
                result["database_name"] = db_match.group(1)
                result["create_database_stmt"] = db_match.group(0)

            # CREATE TABLE 문들을 개별적으로 추출
            # 각 CREATE TABLE 문은 여러 줄에 걸쳐 있고 세미콜론으로 끝남
            table_pattern = r"CREATE TABLE [^;]+;"
            table_matches = re.findall(
                table_pattern, content, re.DOTALL | re.IGNORECASE
            )

            for table_stmt in table_matches:
                # 공백과 개행 정리
                clean_stmt = " ".join(table_stmt.split())
                result["create_table_stmts"].append(clean_stmt)

        except Exception as e:
            result["errors"].append(f"DDL 파일 파싱 오류: {str(e)}")

        return result

    def execute_ddl_statement(self, ddl_stmt: str, description: str = "") -> bool:
        """개별 DDL 문을 실행"""
        try:
            print(f"실행 중: {description}")
            print(f"SQL: {ddl_stmt[:100]}{'...' if len(ddl_stmt) > 100 else ''}")

            self.client.command(ddl_stmt)
            print("✅ 성공")
            return True

        except Exception as e:
            print(f"❌ 실패: {str(e)}")
            return False

    def execute_database_ddl(
        self, ddl_info: Dict, continue_on_error: bool = True
    ) -> Dict:
        """하나의 데이터베이스에 대한 모든 DDL을 실행"""
        db_name = ddl_info["database_name"]
        result = {
            "database_name": db_name,
            "total_statements": 0,
            "successful_statements": 0,
            "failed_statements": 0,
            "errors": [],
        }

        print(f"\n{'='*60}")
        print(f"데이터베이스 처리 중: {db_name}")
        # print(f"{'='*60}")

        # 1. 데이터베이스 생성
        if ddl_info["create_database_stmt"]:
            result["total_statements"] += 1
            success = self.execute_ddl_statement(
                ddl_info["create_database_stmt"], f"데이터베이스 {db_name} 생성"
            )
            if success:
                result["successful_statements"] += 1
            else:
                result["failed_statements"] += 1
                if not continue_on_error:
                    return result

        # 2. 테이블들 생성
        for i, table_stmt in enumerate(ddl_info["create_table_stmts"], 1):
            result["total_statements"] += 1

            # 테이블명 추출
            table_match = re.search(r"CREATE TABLE \w+\.(\w+)", table_stmt)
            table_name = table_match.group(1) if table_match else f"table_{i}"

            success = self.execute_ddl_statement(
                table_stmt,
                f"테이블 {table_name} 생성 ({i}/{len(ddl_info['create_table_stmts'])})",
            )

            if success:
                result["successful_statements"] += 1
            else:
                result["failed_statements"] += 1
                result["errors"].append(f"테이블 {table_name} 생성 실패")
                if not continue_on_error:
                    break

            # 잠시 대기 (서버 부하 방지)
            time.sleep(0.1)

        return result

    def execute_ddl_directory(
        self, ddl_dir_path: Path, continue_on_error: bool = True
    ) -> Dict:
        """DDL 디렉토리의 모든 파일들을 실행"""
        if not ddl_dir_path.exists():
            print(f"DDL 디렉토리가 존재하지 않습니다: {ddl_dir_path}")
            return {}

        ddl_files = list(ddl_dir_path.glob("*_ddl.sql"))

        if not ddl_files:
            print(f"DDL 파일을 찾을 수 없습니다: {ddl_dir_path}")
            return {}

        print(f"총 {len(ddl_files)}개의 DDL 파일을 발견했습니다.")

        overall_results = {
            "total_databases": len(ddl_files),
            "successful_databases": 0,
            "failed_databases": 0,
            "database_results": [],
        }

        for ddl_file in sorted(ddl_files):
            print(f"\n파일 처리 중: {ddl_file.name}")

            # DDL 파일 파싱
            ddl_info = self.parse_ddl_file(ddl_file)

            if ddl_info["errors"]:
                print(f"파일 파싱 실패: {ddl_file.name}")
                for error in ddl_info["errors"]:
                    print(f"  - {error}")
                overall_results["failed_databases"] += 1
                continue

            # DDL 실행
            db_result = self.execute_database_ddl(ddl_info, continue_on_error)
            overall_results["database_results"].append(db_result)

            if db_result["failed_statements"] == 0:
                overall_results["successful_databases"] += 1
            else:
                overall_results["failed_databases"] += 1

        return overall_results

    def execute_single_ddl_file(
        self, ddl_file_path: Path, continue_on_error: bool = True
    ) -> Dict:
        """단일 DDL 파일을 실행"""
        print(f"DDL 파일 실행: {ddl_file_path}")

        # DDL 파일 파싱
        ddl_info = self.parse_ddl_file(ddl_file_path)

        if ddl_info["errors"]:
            print(f"파일 파싱 실패:")
            for error in ddl_info["errors"]:
                print(f"  - {error}")
            return {}

        # DDL 실행
        return self.execute_database_ddl(ddl_info, continue_on_error)

    def print_summary(self, results: Dict):
        """실행 결과 요약 출력"""
        print(f"\n{'='*60}")
        print("실행 결과 요약")
        print(f"{'='*60}")

        if "total_databases" in results:
            # 전체 디렉토리 실행 결과
            print(f"총 데이터베이스: {results['total_databases']}")
            print(f"성공: {results['successful_databases']}")
            print(f"실패: {results['failed_databases']}")

            print(f"\n데이터베이스별 상세 결과:")
            for db_result in results["database_results"]:
                db_name = db_result["database_name"]
                total = db_result["total_statements"]
                success = db_result["successful_statements"]
                failed = db_result["failed_statements"]

                status = (
                    "✅ 성공"
                    if failed == 0
                    else "❌ 부분실패" if success > 0 else "❌ 실패"
                )
                print(f"  {db_name}: {status} ({success}/{total})")

        else:
            # 단일 데이터베이스 실행 결과
            db_name = results["database_name"]
            total = results["total_statements"]
            success = results["successful_statements"]
            failed = results["failed_statements"]

            print(f"데이터베이스: {db_name}")
            print(f"총 DDL 문: {total}")
            print(f"성공: {success}")
            print(f"실패: {failed}")

    def close(self):
        """연결 종료"""
        if self.client:
            self.client.close()


def main():
    """메인 실행 함수"""
    import argparse

    parser = argparse.ArgumentParser(description="ClickHouse DDL 실행기")
    parser.add_argument("--host", default="localhost", help="ClickHouse 호스트")
    parser.add_argument("--port", default=8124, type=int, help="ClickHouse 포트")
    parser.add_argument("--username", default="clickhouse", help="사용자명")
    parser.add_argument("--password", default="clickhouse", help="패스워드")
    parser.add_argument("--ddl-dir", default="clickhouse_ddl", help="DDL 파일 디렉토리")
    parser.add_argument("--single-file", help="단일 DDL 파일 경로")
    parser.add_argument(
        "--continue-on-error", action="store_true", help="오류 발생시에도 계속 진행"
    )

    args = parser.parse_args()

    # DDL Executor 초기화
    try:
        print(args.host, args.port, args.username)
        executor = ClickHouseDDLExecutor(
            host=args.host,
            port=args.port,
            username=args.username,
            password=args.password,
        )

        print(f"ClickHouse 연결 성공: {args.host}:{args.port}")

        if args.single_file:
            # 단일 파일 실행
            file_path = Path(args.single_file)
            if not file_path.exists():
                print(f"파일이 존재하지 않습니다: {file_path}")
                return

            results = executor.execute_single_ddl_file(
                file_path, args.continue_on_error
            )
        else:
            # 디렉토리 전체 실행
            ddl_dir = Path(args.ddl_dir)
            results = executor.execute_ddl_directory(ddl_dir, args.continue_on_error)

        # 결과 요약
        executor.print_summary(results)

    except Exception as e:
        print(f"ClickHouse 연결 실패: {e}")
        return

    finally:
        executor.close()


if __name__ == "__main__":
    # 스크립트로 직접 실행시 간단한 실행
    if len(os.sys.argv) == 1:
        print("ClickHouse DDL 실행기")
        print("=" * 40)

        # 기본 설정으로 실행
        executor = ClickHouseDDLExecutor()

        try:
            print("ClickHouse 연결 테스트...")

            # DDL 디렉토리 확인
            ddl_dir = Path("clickhouse_ddl")
            if ddl_dir.exists():
                print(f"DDL 디렉토리 발견: {ddl_dir}")

                response = input(f"모든 DDL 파일을 실행하시겠습니까? (y/N): ")
                if response.lower() in ["y", "yes"]:
                    results = executor.execute_ddl_directory(
                        ddl_dir, continue_on_error=True
                    )
                    executor.print_summary(results)
                else:
                    print("실행을 취소했습니다.")
            else:
                print(f"DDL 디렉토리를 찾을 수 없습니다: {ddl_dir}")
                print("먼저 DDL 변환기를 실행해주세요.")

        except Exception as e:
            print(f"오류 발생: {e}")

        finally:
            executor.close()
    else:
        main()
