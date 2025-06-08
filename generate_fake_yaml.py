"""
여덟번째 실행되는 파일
generated_data 디렉토리의 CSV 파일들을 분석하여 데이터의 특성을 파악하고,
LangChain을 사용하여 YAML 형식의 데이터 설명을 생성하는 스크립트
"""

import os
import json
from typing import List, Dict, Any
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
import glob
import yaml
import pandas as pd

from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()


class DataAnalyzer:
    def __init__(self, openai_api_key: str):
        self.llm = OpenAI(
            openai_api_key=openai_api_key, temperature=0, model="gpt-4o-mini"
        )

    def analyze_csv_data(self, csv_path: str) -> Dict[str, Any]:
        """CSV 파일의 데이터를 분석하여 컬럼 정보를 추출합니다."""
        try:
            # CSV 파일 읽기 (첫 번째 행만)
            df = pd.read_csv(csv_path, nrows=1)

            # 컬럼 정보 수집
            columns_info = []
            for column in df.columns:
                dtype = str(df[column].dtype)
                columns_info.append({"name": column, "type": dtype})

            return {
                "table_name": os.path.splitext(os.path.basename(csv_path))[0],
                "columns": columns_info,
            }
        except Exception as e:
            print(f"CSV 파일 분석 중 오류 발생: {csv_path} - {str(e)}")
            return None

    def generate_yaml_description(
        self, table_info: Dict[str, Any], db_name: str, max_retries: int = 5
    ) -> str:
        """LangChain을 사용하여 데이터 분석 결과를 바탕으로 YAML 형식의 데이터 설명을 생성합니다."""
        base_prompt = """
You are a tool that analyzes table information and generates YAML format descriptions.

Table Information:
{table_info}

Output Format Requirements:
1. Only output YAML block wrapped with ```yaml and ```
2. No indentation before ```yaml
3. No other text, explanations, or code outside YAML block
4. Must end with exactly three backticks (```)
5. No additional text after closing backticks

YAML Content Requirements:
- All descriptions must be in Korean
- Must include ALL input columns (no omissions)
- Table and column names must be wrapped in double quotes
- No special characters or emojis
- Add appropriate tests based on column role (unique, not_null)

Output Structure Example:
```yaml
name: "테이블명"
description: "테이블에 대한 한국어 설명"
columns:
  - name: "컬럼명"
    description: "컬럼에 대한 한국어 설명"
```
"""

        # 재시도용 분할 프롬프트
        split_first_prompt = """
You are a tool that analyzes table information and generates YAML format descriptions.
This is the FIRST PART - generate table info with FIRST HALF of columns only.

Table Information:
{table_info}

Output Format Requirements:
1. Only output YAML block wrapped with ```yaml and ```
2. No indentation before ```yaml
3. No other text, explanations, or code outside YAML block
4. Must end with exactly three backticks (```)
5. No additional text after closing backticks

YAML Content Requirements:
- All descriptions must be in Korean
- Include ONLY the columns provided in the table information
- Table and column names must be wrapped in double quotes
- No special characters or emojis
- Add appropriate tests based on column role (unique, not_null)

Output Structure Example:
```yaml
name: "테이블명"
description: "테이블에 대한 한국어 설명"
columns:
  - name: "컬럼명"
    description: "컬럼에 대한 한국어 설명"
```
"""

        split_second_prompt = """
You are a tool that generates column descriptions in YAML format.
This is the SECOND PART - generate ONLY the remaining columns.

Columns to add:
{table_info}

Output Format Requirements:
1. Only output YAML block wrapped with ```yaml and ```
2. No indentation before ```yaml
3. No other text, explanations, or code outside YAML block
4. Must end with exactly three backticks (```)
5. No additional text after closing backticks

YAML Content Requirements:
- All descriptions must be in Korean
- Include ONLY the columns provided
- Column names must be wrapped in double quotes
- No special characters or emojis
- Add appropriate tests based on column role (unique, not_null)

Output Structure (COLUMNS ONLY):
```yaml
- name: "컬럼명"
  description: "컬럼에 대한 한국어 설명"
- name: "컬럼명2"
  description: "컬럼에 대한 한국어 설명"
```
"""

        retry_prompt = """
            Previous attempt failed. Here is the incomplete YAML that was generated:
            {previous_response}

            Error message: {error_message}

            Please generate a complete YAML block following the same requirements as before.
            Make sure to:
            1. Include ALL columns
            2. Complete the YAML block properly
            3. End with exactly three backticks (```) on a new line
            4. Do not add any text after the closing backticks
            5. Ensure that all description texts inside the YAML block are properly enclosed in double quotes
            6. Ensure that all `name` field values (table names and column names) are properly enclosed in double quotes
            """

        table_info_str = json.dumps(table_info, indent=2, ensure_ascii=False)
        previous_response = None
        error_message = None

        for attempt in range(max_retries):
            try:
                # 첫 시도: 일반적인 방법
                if attempt == 0:
                    prompt = PromptTemplate(
                        input_variables=["table_info", "db_name"], template=base_prompt
                    )
                    response = self.llm.invoke(
                        prompt.format(table_info=table_info_str, db_name=db_name)
                    )

                # 재시도: 컬럼 분할 방식 사용
                elif attempt >= 1:
                    print(f"=== 재시도 {attempt}: 컬럼 3조각 분할 방식 사용 ===")

                    # 컬럼을 3조각으로 분할
                    columns = table_info["columns"]
                    total_cols = len(columns)

                    # 3등분 인덱스 계산
                    first_end = total_cols // 3
                    second_end = (total_cols * 2) // 3

                    first_part = columns[:first_end]
                    second_part = columns[first_end:second_end]
                    third_part = columns[second_end:]

                    print(f"전체 컬럼 수: {total_cols}")
                    print(f"첫 번째 조각: {len(first_part)}개")
                    print(f"두 번째 조각: {len(second_part)}개")
                    print(f"세 번째 조각: {len(third_part)}개")

                    # 첫 번째 조각으로 기본 YAML 생성 (테이블명 + 첫 번째 1/3 컬럼)
                    first_table_info = {
                        "table_name": table_info["table_name"],
                        "columns": first_part,
                    }
                    first_table_info_str = json.dumps(
                        first_table_info, indent=2, ensure_ascii=False
                    )

                    prompt1 = PromptTemplate(
                        input_variables=["table_info"], template=split_first_prompt
                    )
                    first_response = self.llm.invoke(
                        prompt1.format(table_info=first_table_info_str)
                    )

                    # 첫 번째 응답에서 YAML 추출
                    yaml_start = first_response.find("```yaml")
                    if yaml_start == -1:
                        error_message = (
                            "첫 번째 조각 YAML 블록(```yaml)을 찾을 수 없습니다."
                        )
                        previous_response = first_response
                        raise ValueError(error_message)

                    yaml_content_start = first_response.find("\n", yaml_start) + 1
                    yaml_end = first_response.find("```", yaml_start + 7)
                    if yaml_end == -1:
                        error_message = (
                            "첫 번째 조각 YAML 블록 종료(```)를 찾을 수 없습니다."
                        )
                        previous_response = first_response[yaml_content_start:].strip()
                        raise ValueError(error_message)

                    first_yaml_str = first_response[yaml_content_start:yaml_end].strip()
                    first_yaml_data = yaml.safe_load(first_yaml_str)

                    # 두 번째 조각 처리 (컬럼만)
                    if second_part:
                        second_table_info_str = json.dumps(
                            second_part, indent=2, ensure_ascii=False
                        )

                        prompt2 = PromptTemplate(
                            input_variables=["table_info"], template=split_second_prompt
                        )
                        second_response = self.llm.invoke(
                            prompt2.format(table_info=second_table_info_str)
                        )

                        # 두 번째 응답에서 YAML 추출
                        yaml_start = second_response.find("```yaml")
                        if yaml_start == -1:
                            error_message = (
                                "두 번째 조각 YAML 블록(```yaml)을 찾을 수 없습니다."
                            )
                            previous_response = second_response
                            raise ValueError(error_message)

                        yaml_content_start = second_response.find("\n", yaml_start) + 1
                        yaml_end = second_response.find("```", yaml_start + 7)
                        if yaml_end == -1:
                            error_message = (
                                "두 번째 조각 YAML 블록 종료(```)를 찾을 수 없습니다."
                            )
                            previous_response = second_response[
                                yaml_content_start:
                            ].strip()
                            raise ValueError(error_message)

                        second_yaml_str = second_response[
                            yaml_content_start:yaml_end
                        ].strip()
                        second_columns = yaml.safe_load(second_yaml_str)

                        # 두 번째 조각을 첫 번째에 합치기
                        if isinstance(second_columns, list):
                            first_yaml_data["columns"].extend(second_columns)
                        else:
                            error_message = (
                                "두 번째 조각이 올바른 컬럼 리스트 형식이 아닙니다."
                            )
                            previous_response = second_yaml_str
                            raise ValueError(error_message)

                    # 세 번째 조각 처리 (컬럼만)
                    if third_part:
                        third_table_info_str = json.dumps(
                            third_part, indent=2, ensure_ascii=False
                        )

                        prompt3 = PromptTemplate(
                            input_variables=["table_info"], template=split_second_prompt
                        )
                        third_response = self.llm.invoke(
                            prompt3.format(table_info=third_table_info_str)
                        )

                        # 세 번째 응답에서 YAML 추출
                        yaml_start = third_response.find("```yaml")
                        if yaml_start == -1:
                            error_message = (
                                "세 번째 조각 YAML 블록(```yaml)을 찾을 수 없습니다."
                            )
                            previous_response = third_response
                            raise ValueError(error_message)

                        yaml_content_start = third_response.find("\n", yaml_start) + 1
                        yaml_end = third_response.find("```", yaml_start + 7)
                        if yaml_end == -1:
                            error_message = (
                                "세 번째 조각 YAML 블록 종료(```)를 찾을 수 없습니다."
                            )
                            previous_response = third_response[
                                yaml_content_start:
                            ].strip()
                            raise ValueError(error_message)

                        third_yaml_str = third_response[
                            yaml_content_start:yaml_end
                        ].strip()
                        third_columns = yaml.safe_load(third_yaml_str)

                        # 세 번째 조각을 첫 번째에 합치기
                        if isinstance(third_columns, list):
                            first_yaml_data["columns"].extend(third_columns)
                        else:
                            error_message = (
                                "세 번째 조각이 올바른 컬럼 리스트 형식이 아닙니다."
                            )
                            previous_response = third_yaml_str
                            raise ValueError(error_message)

                    # 합쳐진 데이터를 문자열로 변환
                    response = (
                        "```yaml\n"
                        + yaml.dump(
                            first_yaml_data,
                            allow_unicode=True,
                            sort_keys=False,
                            default_flow_style=False,
                        )
                        + "```"
                    )

                # 기존 재시도 로직 (백업용)
                else:
                    prompt = PromptTemplate(
                        input_variables=[
                            "table_info",
                            "db_name",
                            "previous_response",
                            "error_message",
                        ],
                        template=retry_prompt,
                    )
                    response = self.llm.invoke(
                        prompt.format(
                            table_info=table_info_str,
                            db_name=db_name,
                            previous_response=previous_response,
                            error_message=error_message,
                        )
                    )
                    print(response)

                # 응답에서 YAML 블록 추출 (정확한 위치 찾기)
                yaml_start = response.find("```yaml")
                if yaml_start == -1:
                    error_message = "YAML 블록(```yaml)을 찾을 수 없습니다."
                    previous_response = response
                    raise ValueError(error_message)

                # ```yaml 다음 줄부터 시작
                yaml_content_start = response.find("\n", yaml_start) + 1
                yaml_end = response.find("```", yaml_start + 7)
                if yaml_end == -1:
                    print("종료 백틱이 없는 경우, YAML 내용이 완성되어 있는지 확인")
                    # 종료 백틱이 없는 경우, YAML 내용이 완성되어 있는지 확인
                    potential_yaml = response[yaml_content_start:].strip()
                    try:
                        print("=== YAML 파싱 시도 ===")
                        # YAML 파싱 시도
                        yaml_data = yaml.safe_load(potential_yaml)
                        print(f"파싱 성공: {type(yaml_data)}")

                        # 기본 구조 검증
                        if (
                            isinstance(yaml_data, dict)
                            and "name" in yaml_data
                            and "columns" in yaml_data
                            and isinstance(yaml_data["columns"], list)
                        ):

                            print("=== 기본 구조 검증 통과 ===")
                            print(f"테이블명: {yaml_data.get('name')}")
                            print(f"컬럼 수: {len(yaml_data['columns'])}")

                            # 모든 컬럼이 포함되어 있는지 확인
                            input_columns = {
                                col["name"] for col in table_info["columns"]
                            }
                            # YAML 파싱 시 No/Yes 등이 boolean으로 변환되는 문제 해결
                            output_columns = {
                                str(col["name"]) for col in yaml_data["columns"]
                            }

                            print(f"입력 컬럼: {input_columns}")
                            print(f"출력 컬럼: {output_columns}")

                            if input_columns == output_columns:
                                print("=== 컬럼 검증 통과! 백틱 추가하여 성공 처리 ===")
                                # YAML이 완성되어 있으므로 백틱만 추가하여 성공 처리
                                yaml_str = potential_yaml
                                return yaml.dump(
                                    yaml_data,
                                    allow_unicode=True,
                                    sort_keys=False,
                                    default_flow_style=False,
                                )
                            else:
                                missing = input_columns - output_columns
                                extra = output_columns - input_columns
                                print(f"=== 컬럼 불일치 ===")
                                print(f"누락: {missing}")
                                print(f"추가: {extra}")
                        else:
                            print("=== 기본 구조 검증 실패 ===")
                            print(
                                f"isinstance(yaml_data, dict): {isinstance(yaml_data, dict)}"
                            )
                            print(
                                f"'name' in yaml_data: {'name' in yaml_data if isinstance(yaml_data, dict) else False}"
                            )
                            print(
                                f"'columns' in yaml_data: {'columns' in yaml_data if isinstance(yaml_data, dict) else False}"
                            )
                            print(
                                f"isinstance columns list: {isinstance(yaml_data.get('columns'), list) if isinstance(yaml_data, dict) else False}"
                            )
                    except yaml.YAMLError as e:
                        print(f"=== YAML 파싱 실패 ===")
                        print(f"오류: {e}")
                        pass  # YAML 파싱 실패 시 기존 로직 유지
                    except Exception as e:
                        print(f"=== 예상치 못한 오류 ===")
                        print(f"오류: {e}")
                        pass

                    # 기존 오류 처리
                    error_message = "YAML 블록 종료(```)를 찾을 수 없습니다."
                    previous_response = response[yaml_content_start:].strip()
                    raise ValueError(error_message)

                # YAML 블록 추출 및 전처리
                yaml_str = response[yaml_content_start:yaml_end].strip()

                # YAML 형식 검증
                try:
                    yaml_data = yaml.safe_load(yaml_str)
                    if not isinstance(yaml_data, dict):
                        error_message = "YAML 데이터가 딕셔너리 형식이 아닙니다."
                        previous_response = yaml_str
                        raise ValueError(error_message)
                    if "name" not in yaml_data:
                        error_message = "YAML에 'name' 필드가 없습니다."
                        previous_response = yaml_str
                        raise ValueError(error_message)
                    if "columns" not in yaml_data:
                        error_message = "YAML에 'columns' 필드가 없습니다."
                        previous_response = yaml_str
                        raise ValueError(error_message)

                    # 모든 컬럼이 포함되어 있는지 확인
                    input_columns = {col["name"] for col in table_info["columns"]}
                    output_columns = {str(col["name"]) for col in yaml_data["columns"]}
                    if input_columns != output_columns:
                        missing_columns = input_columns - output_columns
                        extra_columns = output_columns - input_columns
                        error_msg = []
                        if missing_columns:
                            error_msg.append(f"누락된 컬럼: {missing_columns}")
                        if extra_columns:
                            error_msg.append(f"추가된 컬럼: {extra_columns}")
                        error_message = "컬럼 불일치: " + ", ".join(error_msg)
                        previous_response = yaml_str
                        raise ValueError(error_message)

                    # YAML 데이터를 다시 문자열로 변환하여 반환
                    return yaml.dump(
                        yaml_data,
                        allow_unicode=True,
                        sort_keys=False,
                        default_flow_style=False,
                    )
                except yaml.YAMLError as e:
                    error_message = f"YAML 형식이 올바르지 않습니다: {str(e)}"
                    previous_response = yaml_str
                    print(
                        f"YAML 파싱 실패 (시도 {attempt + 1}/{max_retries}). 원본 YAML:\n{yaml_str}"
                    )
                    if attempt == max_retries - 1:
                        raise ValueError(error_message)
                    continue

            except Exception as e:
                print(
                    f"LLM 응답 처리 중 오류 발생 (시도 {attempt + 1}/{max_retries}): {str(e)}"
                )
                if attempt == max_retries - 1:
                    print(f"최종 시도 실패. 원본 응답: {response}")
                    raise
                print("재시도합니다...")
                continue

        raise ValueError(f"최대 재시도 횟수({max_retries})를 초과했습니다.")


def main():
    # 환경 변수에서 API 키 가져오기
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY 환경 변수가 설정되어 있지 않습니다.")

    analyzer = DataAnalyzer(openai_api_key)

    # 생성된 YAML을 저장할 디렉토리 생성
    yaml_dir = "generated_yaml"
    os.makedirs(yaml_dir, exist_ok=True)

    # 데이터베이스별로 YAML 데이터를 저장할 딕셔너리
    db_yaml_data = {}

    # generated_data 디렉토리 내의 모든 CSV 파일 처리
    csv_files = glob.glob("generated_data/**/*.csv", recursive=True)

    for csv_file in csv_files:
        print(f"처리 중인 CSV 파일: {csv_file}")

        # CSV 파일이 있는 디렉토리 경로 추출
        csv_dir = os.path.dirname(csv_file)
        relative_path = os.path.relpath(csv_dir, "generated_data")
        db_name = os.path.basename(csv_dir)  # 디렉토리명을 데이터베이스명으로 사용

        # 생성된 YAML을 저장할 디렉토리 경로 설정
        output_dir = os.path.join(yaml_dir, relative_path)
        os.makedirs(output_dir, exist_ok=True)

        # YAML 파일 경로 설정
        yaml_file_path = os.path.join(output_dir, "sources.yml")

        # CSV 데이터 분석
        table_info = analyzer.analyze_csv_data(csv_file)
        if not table_info:
            continue

        # 데이터베이스별 YAML 데이터 초기화 또는 가져오기
        if db_name not in db_yaml_data:
            # 기존 YAML 파일이 있다면 로드
            if os.path.exists(yaml_file_path):
                try:
                    with open(yaml_file_path, "r", encoding="utf-8") as f:
                        existing_data = yaml.safe_load(f)
                        # 기존 데이터의 구조가 올바른지 확인
                        if (
                            isinstance(existing_data, dict)
                            and "sources" in existing_data
                            and len(existing_data["sources"]) > 0
                            and "tables" in existing_data["sources"][0]
                        ):
                            db_yaml_data[db_name] = existing_data
                        else:
                            raise ValueError(
                                "기존 YAML 파일의 구조가 올바르지 않습니다."
                            )
                except Exception as e:
                    print(f"기존 YAML 파일 로드 중 오류 발생: {e}")
                    # 오류 발생 시 새로운 구조로 초기화
                    db_yaml_data[db_name] = {
                        "version": 2,
                        "sources": [
                            {
                                "name": db_name,
                                "description": f"{db_name} 데이터셋의 테이블 모음",
                                "database": db_name,
                                "tables": [],
                            }
                        ],
                    }
            else:
                # 새로운 YAML 데이터 구조 초기화
                db_yaml_data[db_name] = {
                    "version": 2,
                    "sources": [
                        {
                            "name": db_name,
                            "description": f"{db_name} 데이터셋의 테이블 모음",
                            "database": db_name,
                            "tables": [],
                        }
                    ],
                }

        # 테이블이 이미 존재하는지 먼저 확인
        existing_tables = db_yaml_data[db_name]["sources"][0]["tables"]
        table_exists = any(
            t.get("name") == table_info["table_name"] for t in existing_tables
        )

        if table_exists:
            print(f"테이블이 이미 존재함: {table_info['table_name']}, 건너뜁니다.")
            continue

        # YAML 설명 생성 (테이블이 존재하지 않는 경우에만)
        try:
            yaml_description = analyzer.generate_yaml_description(table_info, db_name)
            table_data = yaml.safe_load(yaml_description)

            # 테이블 데이터를 sources의 tables 리스트에 추가
            existing_tables.append(table_data)
            print(f"새로운 테이블 추가: {table_data['name']}")

            # YAML 파일로 저장
            with open(yaml_file_path, "w", encoding="utf-8") as f:
                yaml.dump(
                    db_yaml_data[db_name],
                    f,
                    allow_unicode=True,
                    sort_keys=False,
                    default_flow_style=False,
                )
            print(f"YAML 파일 업데이트 완료: {yaml_file_path}")

        except Exception as e:
            print(f"테이블 '{table_info['table_name']}' 처리 중 오류 발생: {str(e)}")
            continue


if __name__ == "__main__":
    main()
