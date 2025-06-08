"""
네번째 실행되는 파일
spider_data/database 디렉토리 하위의 모든 SQLite 파일을 분석하여 테이블 스키마를 분석하고,
LangChain을 사용하여 테이블 스키마에 맞는 Faker 코드를 생성하는 스크립트
"""

import os
import sqlite3
import json
from typing import List, Dict, Any
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from faker import Faker
import pandas as pd
from clickhouse_driver import Client
import glob

from dotenv import load_dotenv

# from data_inserter import DataInserter

load_dotenv()


class SchemaAnalyzer:
    def __init__(self, openai_api_key: str):
        self.llm = OpenAI(
            openai_api_key=openai_api_key, temperature=0, model="gpt-4o-mini"
        )
        self.faker = Faker()

    def get_table_schema(self, db_path: str) -> Dict[str, List[Dict[str, str]]]:
        """SQLite 데이터베이스의 테이블 스키마를 분석합니다."""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 모든 테이블 이름 가져오기
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            schema[table_name] = [
                {
                    "name": col[1],
                    "type": col[2],
                    "notnull": bool(col[3]),
                    "dflt_value": col[4],
                    "pk": bool(col[5]),
                }
                for col in columns
            ]

        conn.close()
        return schema

    def generate_faker_code(self, table_name: str, schema: List[Dict[str, str]]) -> str:
        """LangChain을 사용하여 테이블 스키마에 맞는 Faker 코드를 생성합니다."""
        prompt = PromptTemplate(
            input_variables=["table_name", "schema"],
            template="""
            테이블 '{table_name}'의 스키마에 맞는 Python Faker 코드를 생성해주세요.
            스키마 정보:
            {schema}
            
            다음 형식으로 코드를 생성해주세요:
            1. 각 컬럼에 대해 적절한 Faker 메서드를 선택
            2. 데이터 타입에 맞는 변환 로직 포함 하지만 None 값은 생성하지 않도록 해주세요
            3. 필요한 import 문 포함
            4. 함수는 generate_fake_data() 형태로 반환하고, 데이터를 딕셔너리 리스트로 반환하도록 해주세요
            5. 컬럼 이름은 원본 데이터베이스의 컬럼 이름을 그대로 사용해주세요
            6. 코드블럭으로 감싸지 않고 코드만 반환해주세요
            7. num_records 파라미터를 받아서 그 수만큼 데이터를 생성해주세요
            9. datetime 타입은 date_time_this_year() 함수를 사용해주세요
            
            코드만 반환해주세요.
            """,
        )

        schema_str = json.dumps(schema, indent=2, ensure_ascii=False)
        response = self.llm(prompt.format(table_name=table_name, schema=schema_str))
        return response


def main():
    # 환경 변수에서 API 키 가져오기
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY 환경 변수가 설정되어 있지 않습니다.")

    analyzer = SchemaAnalyzer(openai_api_key)

    # 생성된 데이터를 저장할 디렉토리 생성
    data_dir = "generated_data"
    os.makedirs(data_dir, exist_ok=True)

    # database 디렉토리 내의 모든 SQLite 파일 처리
    db_files = glob.glob("spider_data/database/**/*.sqlite", recursive=True)

    for db_file in db_files:
        print(f"처리 중인 데이터베이스: {db_file}")

        # 데이터베이스 디렉토리 경로 추출
        db_dir = os.path.dirname(db_file)
        relative_path = os.path.relpath(db_dir, "spider_data/database")

        # 생성된 코드를 저장할 디렉토리 경로 설정
        output_dir = os.path.join("temp_faker_code", relative_path)
        os.makedirs(output_dir, exist_ok=True)

        # 스키마 분석
        schema = analyzer.get_table_schema(db_file)

        for table_name, table_schema in schema.items():
            print(f"테이블 처리 중: {table_name}")

            # 임시 파일 경로 설정 (데이터베이스 디렉토리 구조 유지)
            temp_file_path = os.path.join(output_dir, f"temp_faker_{table_name}.py")

            # 파일이 이미 존재하는 경우 건너뛰기
            if os.path.exists(temp_file_path):
                print(f"파일이 이미 존재합니다: {temp_file_path}")
                continue

            # Faker 코드 생성
            faker_code = analyzer.generate_faker_code(table_name, table_schema)

            # 생성된 코드를 임시 파일로 저장하고 실행
            with open(temp_file_path, "w") as f:
                f.write(faker_code)


if __name__ == "__main__":
    main()
