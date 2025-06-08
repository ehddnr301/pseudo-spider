"""
두번째 실행되는 파일
sqlite 파일을 clickhouse ddl로 변환하는 프로그램
sqlite 파일은 spider_data/database 디렉토리에 있음
clickhouse ddl 파일은 clickhouse_ddl 디렉토리에 저장됨

sqlite 파일은 데이터베이스 파일이며, 테이블 정보가 포함되어 있음
clickhouse ddl 파일은 clickhouse 데이터베이스에 테이블을 생성하는 데 사용됨

sqlite 파일은 데이터베이스 파일이며, 테이블 정보가 포함되어 있음
clickhouse ddl 파일은 clickhouse 데이터베이스에 테이블을 생성하는 데 사용됨
"""

import os
import re
import sqlite3
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class SQLiteToClickHouseConverter:
    """SQLite 스키마를 ClickHouse DDL로 변환하는 클래스"""

    def __init__(self):
        self.type_mapping = {
            # SQLite 타입 -> ClickHouse 타입 매핑
            "INTEGER": "Int64",
            "INT": "Int32",
            "BIGINT": "Int64",
            "SMALLINT": "Int16",
            "TINYINT": "Int8",
            "REAL": "Float64",
            "FLOAT": "Float32",
            "DOUBLE": "Float64",
            "TEXT": "String",
            "VARCHAR": "String",
            "CHAR": "String",
            "BLOB": "String",
            "NUMERIC": "Decimal64(2)",
            "DECIMAL": "Decimal64(2)",
            "DATE": "Date",
            "DATETIME": "DateTime",
            "TIMESTAMP": "DateTime",
            "BOOLEAN": "UInt8",
            "BOOL": "UInt8",
        }

    def safe_identifier(self, identifier: str) -> str:
        """ClickHouse에서 안전한 식별자로 변환 (항상 백틱으로 감싸기)"""
        # 모든 식별자를 백틱으로 감싸서 특수문자, 예약어, 공백 등 모든 문제 방지
        identifier = identifier.strip()

        # 이미 백틱으로 감싸져 있는 경우 중복 방지
        if identifier.startswith("`") and identifier.endswith("`"):
            return identifier

        return f"`{identifier}`"

    def parse_sql_file(self, sql_file_path: Path) -> List[Dict]:
        """SQL 파일을 읽어서 CREATE TABLE 문들을 파싱하여 테이블 정보 추출"""
        try:
            with open(sql_file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(sql_file_path, "r", encoding="latin-1") as f:
                content = f.read()

        # CREATE TABLE 문들을 찾기
        create_table_pattern = r"CREATE\s+TABLE\s+[^;]+;"
        create_tables = re.findall(
            create_table_pattern, content, re.IGNORECASE | re.DOTALL
        )

        tables_info = []
        for create_stmt in create_tables:
            table_info = self.parse_create_table_statement(create_stmt)
            if table_info:
                tables_info.append(table_info)

        return tables_info

    def parse_create_table_statement(self, create_stmt: str) -> Optional[Dict]:
        """CREATE TABLE 문을 파싱하여 테이블 정보 추출"""
        try:
            # 테이블명 추출 - 따옴표 처리 개선
            table_name_pattern = r'CREATE\s+TABLE\s+["`]?([^"`\s\(]+)["`]?'
            table_match = re.search(table_name_pattern, create_stmt, re.IGNORECASE)
            if not table_match:
                return None

            table_name = table_match.group(1)

            # 컬럼 정의 부분 추출
            columns_part = re.search(r"\((.*)\)", create_stmt, re.DOTALL)
            if not columns_part:
                return None

            columns_text = columns_part.group(1)

            # Primary key 추출
            pk_pattern = r'primary\s+key\s*\(\s*["`]?([^)]+)["`]?\s*\)'
            pk_match = re.search(pk_pattern, columns_text, re.IGNORECASE)
            primary_keys = []
            if pk_match:
                pk_text = pk_match.group(1)
                primary_keys = [
                    col.strip().strip('"').strip("`").strip()
                    for col in pk_text.split(",")
                ]

            # Foreign key와 primary key 제약조건 제거
            clean_columns_text = re.sub(
                r",?\s*foreign\s+key[^,)]+(?:,|(?=\)))",
                "",
                columns_text,
                flags=re.IGNORECASE,
            )
            clean_columns_text = re.sub(
                r",?\s*primary\s+key[^,)]+(?:,|(?=\)))",
                "",
                clean_columns_text,
                flags=re.IGNORECASE,
            )

            # 개별 컬럼 정의 파싱
            columns = []

            # 컬럼 정의들을 더 정확히 분리
            # 중첩된 괄호와 쉼표를 고려한 파싱
            column_definitions = self.split_column_definitions(clean_columns_text)

            for col_def in column_definitions:
                col_def = col_def.strip()
                if not col_def or any(
                    keyword in col_def.lower()
                    for keyword in ["foreign key", "primary key", "constraint"]
                ):
                    continue

                # 컬럼명과 타입 추출 - 개선된 파싱
                parts = col_def.strip().split()
                if len(parts) >= 2:
                    col_name = parts[0].strip('"').strip("`").strip()
                    col_type = parts[1].strip()

                    # 컬럼명이 비어있지 않은지 확인
                    if col_name and col_type:
                        columns.append(
                            {
                                "name": col_name,
                                "type": col_type,
                                "nullable": col_name not in primary_keys,
                                "primary_key": col_name in primary_keys,
                                "default": None,
                            }
                        )

            return {"name": table_name, "columns": columns}

        except Exception as e:
            print(f"CREATE TABLE 문 파싱 오류: {e}")
            print(f"문제가 된 SQL: {create_stmt[:200]}...")
            return None

    def split_column_definitions(self, columns_text: str) -> List[str]:
        """컬럼 정의들을 정확히 분리하는 헬퍼 메서드"""
        definitions = []
        current_def = ""
        paren_count = 0

        for char in columns_text:
            if char == "(":
                paren_count += 1
            elif char == ")":
                paren_count -= 1
            elif char == "," and paren_count == 0:
                if current_def.strip():
                    definitions.append(current_def.strip())
                current_def = ""
                continue

            current_def += char

        # 마지막 정의 추가
        if current_def.strip():
            definitions.append(current_def.strip())

        return definitions

    def parse_sqlite_db(self, sqlite_file_path: Path) -> List[Dict]:
        """SQLite 데이터베이스에서 테이블 스키마 정보 추출"""
        tables_info = []

        try:
            conn = sqlite3.connect(str(sqlite_file_path))
            cursor = conn.cursor()

            # 모든 테이블 목록 가져오기
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_names = [row[0] for row in cursor.fetchall()]

            for table_name in table_names:
                # 테이블 스키마 정보 가져오기
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns_info = cursor.fetchall()

                columns = []
                for col_info in columns_info:
                    cid, name, data_type, not_null, default_value, pk = col_info
                    columns.append(
                        {
                            "name": name,
                            "type": data_type,
                            "nullable": not not_null,
                            "primary_key": bool(pk),
                            "default": default_value,
                        }
                    )

                tables_info.append({"name": table_name, "columns": columns})

            conn.close()

        except Exception as e:
            print(f"SQLite 파일 파싱 오류 ({sqlite_file_path}): {e}")

        return tables_info

    def convert_data_type(self, sqlite_type: str) -> str:
        """SQLite 데이터 타입을 ClickHouse 타입으로 변환"""
        sqlite_type = sqlite_type.upper().strip()

        # 괄호가 있는 타입 처리 (예: VARCHAR(255))
        base_type = re.split(r"[\(\s]", sqlite_type)[0]

        # 길이 정보 추출
        length_match = re.search(r"\((\d+)\)", sqlite_type)
        length = int(length_match.group(1)) if length_match else None

        # 타입 매핑
        if base_type in self.type_mapping:
            ch_type = self.type_mapping[base_type]

            # String 타입에 길이 제한이 있는 경우
            # ClickHouse는 FixedString(256) 초과를 허용하지 않으므로 String 사용
            if ch_type == "String" and length and length <= 256:
                # ch_type = f'FixedString({length})'
                ch_type = "String"
            elif ch_type == "String" and length and length > 256:
                # 256바이트 초과는 일반 String 사용
                ch_type = "String"

            return ch_type
        else:
            # 알 수 없는 타입은 String으로 처리
            return "String"

    def convert_default_value(self, default_value) -> Optional[str]:
        """SQLite 기본값을 ClickHouse 기본값으로 변환"""
        if default_value is None:
            return None

        default_str = str(default_value).upper().strip()

        # NULL 기본값은 제거 (Nullable 타입에서는 불필요)
        if default_str in ["NULL", "NONE", ""]:
            return None

        # CURRENT_TIMESTAMP를 now()로 변경
        if "CURRENT_TIMESTAMP" in default_str:
            return "now()"

        # 기타 SQLite 함수들을 ClickHouse 함수로 변경
        replacements = {
            "DATETIME('NOW')": "now()",
            "DATE('NOW')": "today()",
            "STRFTIME": "formatDateTime",
        }

        for sqlite_func, ch_func in replacements.items():
            if sqlite_func in default_str:
                return ch_func

        # 숫자나 문자열 리터럴은 그대로 반환
        return default_value

    def generate_clickhouse_ddl(self, table_info: Dict, database_name: str) -> str:
        """테이블 정보를 기반으로 ClickHouse DDL 생성"""
        table_name = table_info["name"]
        columns = table_info["columns"]

        # 빈 컬럼 리스트 체크
        if not columns:
            print(f"경고: 테이블 {table_name}에 컬럼이 없습니다.")
            return f"-- 스키마 오류: {table_name} 테이블에 컬럼이 없음"

        # 테이블명과 데이터베이스명을 안전한 식별자로 변환
        safe_db_name = self.safe_identifier(database_name)
        safe_table_name = self.safe_identifier(table_name)

        ddl_lines = []
        ddl_lines.append(f"CREATE TABLE {safe_db_name}.{safe_table_name} (")

        column_definitions = []
        non_nullable_columns = []
        primary_key_columns = []

        for i, col in enumerate(columns):
            col_name = col["name"]

            # 빈 컬럼명 체크
            if not col_name or not col_name.strip():
                print(f"경고: 테이블 {table_name}에서 빈 컬럼명 발견, 건너뛰기")
                continue

            safe_col_name = self.safe_identifier(col_name.strip())
            ch_type = self.convert_data_type(col["type"])

            # Primary Key 컬럼 수집
            if col["primary_key"]:
                primary_key_columns.append(safe_col_name)

            # Nullable 처리
            if col["nullable"] and not col["primary_key"]:
                ch_type = f"Nullable({ch_type})"
            else:
                # Nullable이 아닌 컬럼들을 ORDER BY 후보로 수집
                non_nullable_columns.append(safe_col_name)

            # 기본값 처리 - NULL과 문제가 있는 기본값은 제거
            default_clause = ""
            if col["default"] is not None:
                converted_default = self.convert_default_value(col["default"])
                # NULL, CURRENT_TIMESTAMP, 빈 값은 기본값에서 제외
                if converted_default and converted_default.upper() not in [
                    "NULL",
                    "CURRENT_TIMESTAMP",
                    "",
                ]:
                    default_clause = f" DEFAULT {converted_default}"

            column_definitions.append(f"    {safe_col_name} {ch_type}{default_clause}")

        # 컬럼 정의가 비어있는지 최종 체크
        if not column_definitions:
            print(f"오류: 테이블 {table_name}에 유효한 컬럼이 없습니다.")
            return f"-- 오류: {table_name} 테이블에 유효한 컬럼이 없음"

        ddl_lines.append(",\n".join(column_definitions))
        ddl_lines.append(")")

        # ENGINE과 ORDER BY 추가
        ddl_lines.append("ENGINE = MergeTree()")

        # ORDER BY 절 생성 - Nullable 컬럼 제외
        order_by_candidates = []

        if primary_key_columns:
            # Primary Key가 있으면 그것을 ORDER BY로 사용 (이미 non-nullable)
            order_by_candidates = primary_key_columns
        else:
            # Primary Key가 없으면 non-nullable 컬럼들 중에서 선택
            order_by_candidates = non_nullable_columns

        if order_by_candidates:
            if len(order_by_candidates) == 1:
                ddl_lines.append(f"ORDER BY {order_by_candidates[0]};")
            else:
                # 복합키인 경우
                order_by = f"({', '.join(order_by_candidates)})"
                ddl_lines.append(f"ORDER BY {order_by};")
        else:
            # 모든 컬럼이 Nullable인 경우 tuple() 사용
            ddl_lines.append("ORDER BY tuple();")

        return "\n".join(ddl_lines)

    def process_database_directory(self, db_dir_path: Path) -> Dict:
        """데이터베이스 디렉토리를 처리하여 DDL 생성"""
        db_name = db_dir_path.name
        result = {
            "database_name": db_name,
            "sqlite_file": None,
            "sql_file": None,
            "ddl_statements": [],
            "errors": [],
        }

        # .sqlite 파일과 .sql 파일 찾기
        sqlite_files = list(db_dir_path.glob("*.sqlite"))
        sql_files = list(db_dir_path.glob("*.sql"))

        if sqlite_files:
            result["sqlite_file"] = sqlite_files[0]

        if sql_files:
            result["sql_file"] = sql_files[0]

        try:
            if result["sqlite_file"]:
                # SQLite 파일에서 스키마 추출
                tables_info = self.parse_sqlite_db(result["sqlite_file"])

                for table_info in tables_info:
                    ddl = self.generate_clickhouse_ddl(table_info, db_name)
                    result["ddl_statements"].append(ddl)

            elif result["sql_file"]:
                # SQL 파일에서 CREATE TABLE 문 추출 및 변환
                tables_info = self.parse_sql_file(result["sql_file"])

                for table_info in tables_info:
                    ddl = self.generate_clickhouse_ddl(table_info, db_name)
                    result["ddl_statements"].append(ddl)

            else:
                result["errors"].append("SQLite 파일과 SQL 파일을 찾을 수 없습니다.")

        except Exception as e:
            result["errors"].append(f"처리 중 오류 발생: {str(e)}")

        return result


def main():
    """메인 실행 함수"""
    converter = SQLiteToClickHouseConverter()
    spider_db_path = Path("spider_data/database")

    if not spider_db_path.exists():
        print(f"경로가 존재하지 않습니다: {spider_db_path}")
        return

    output_dir = Path("clickhouse_ddl")
    output_dir.mkdir(exist_ok=True)

    total_databases = 0
    successful_conversions = 0
    failed_conversions = 0

    print("SQLite to ClickHouse DDL 변환을 시작합니다...")
    print("=" * 60)

    # 각 데이터베이스 디렉토리 처리
    for db_dir in spider_db_path.iterdir():
        if db_dir.is_dir():
            total_databases += 1
            print(f"\n처리 중: {db_dir.name}")

            result = converter.process_database_directory(db_dir)

            if result["errors"]:
                failed_conversions += 1
                print(f"❌ 실패: {db_dir.name}")
                for error in result["errors"]:
                    print(f"   - {error}")
            else:
                successful_conversions += 1
                print(
                    f"✅ 성공: {db_dir.name} ({len(result['ddl_statements'])}개 테이블)"
                )

                # DDL 파일 저장
                output_file = output_dir / f"{db_dir.name}_ddl.sql"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f"-- ClickHouse DDL for database: {db_dir.name}\n")
                    f.write(
                        f"-- Generated from: {result['sqlite_file'] or result['sql_file']}\n\n"
                    )
                    f.write(f"CREATE DATABASE IF NOT EXISTS {db_dir.name};\n\n")

                    for ddl in result["ddl_statements"]:
                        f.write(ddl + "\n\n")

    # 결과 요약
    print(f"\n{'='*60}")
    print(f"변환 완료!")
    print(f"총 데이터베이스: {total_databases}")
    print(f"성공: {successful_conversions}")
    print(f"실패: {failed_conversions}")
    print(f"DDL 파일 저장 위치: {output_dir}")


if __name__ == "__main__":
    main()
