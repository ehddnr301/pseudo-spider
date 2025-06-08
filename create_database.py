"""
첫번째 실행되는 파일
spider_data/database 디렉토리 하위의 모든 디렉토리명으로 ClickHouse 데이터베이스를 생성
"""

import os
import clickhouse_connect
from pathlib import Path


def create_clickhouse_databases():
    """
    spider_data/database 디렉토리 하위의 모든 디렉토리명으로 ClickHouse 데이터베이스를 생성
    """

    # ClickHouse 연결 설정 (필요에 따라 수정)
    client = clickhouse_connect.get_client(
        host="localhost",
        port=8123,
        username="clickhouse",
        password="clickhouse",  # 필요시 패스워드 입력
    )

    # spider_data/database 경로 설정
    database_path = Path("spider_data/database")

    # 경로가 존재하는지 확인
    if not database_path.exists():
        print(f"경로가 존재하지 않습니다: {database_path}")
        return

    # 생성된 데이터베이스 목록
    created_databases = []
    failed_databases = []

    try:
        # database 디렉토리 하위의 모든 디렉토리 읽기
        for item in database_path.iterdir():
            if item.is_dir():
                db_name = item.name

                try:
                    # 데이터베이스 생성 쿼리 (디렉토리명 그대로 사용)
                    create_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"

                    # 쿼리 실행
                    client.command(create_query)
                    created_databases.append(db_name)
                    print(f"✅ 데이터베이스 생성 완료: {db_name}")

                except Exception as e:
                    failed_databases.append((db_name, str(e)))
                    print(f"❌ 데이터베이스 생성 실패: {db_name} - {e}")

        # 결과 요약
        print(f"\n=== 결과 요약 ===")
        print(f"총 디렉토리 수: {len(created_databases) + len(failed_databases)}")
        print(f"생성 성공: {len(created_databases)}개")
        print(f"생성 실패: {len(failed_databases)}개")

        if created_databases:
            print(f"\n생성된 데이터베이스:")
            for db in created_databases:
                print(f"  - {db}")

        if failed_databases:
            print(f"\n실패한 데이터베이스:")
            for db, error in failed_databases:
                print(f"  - {db}: {error}")

    except Exception as e:
        print(f"전체 프로세스 실행 중 오류 발생: {e}")

    finally:
        # 연결 종료
        client.close()


def list_spider_directories():
    """
    spider_data/database 디렉토리 하위의 모든 디렉토리 목록을 출력
    """
    database_path = Path("spider_data/database")

    if not database_path.exists():
        print(f"경로가 존재하지 않습니다: {database_path}")
        return []

    directories = []
    for item in database_path.iterdir():
        if item.is_dir():
            directories.append(item.name)

    print(f"발견된 디렉토리 수: {len(directories)}")
    print("디렉토리 목록:")
    for i, dir_name in enumerate(sorted(directories), 1):
        print(f"  {i:3d}. {dir_name}")

    return directories


if __name__ == "__main__":
    print("Spider 데이터베이스 디렉토리 목록:")
    print("=" * 50)

    # 먼저 디렉토리 목록 확인
    directories = list_spider_directories()

    if directories:
        print("\n" + "=" * 50)
        print("ClickHouse 데이터베이스 생성을 시작합니다...")

        # 사용자 확인
        response = input(
            f"\n{len(directories)}개의 데이터베이스를 생성하시겠습니까? (y/N): "
        )

        if response.lower() in ["y", "yes"]:
            create_clickhouse_databases()
        else:
            print("데이터베이스 생성을 취소했습니다.")
    else:
        print("생성할 데이터베이스가 없습니다.")
