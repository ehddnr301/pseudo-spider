#!/usr/bin/env python3

import subprocess
import json
import os
import requests
import time
import yaml
import glob
from pathlib import Path

# DataHub 설정
DATAHUB_GMS_URL = "http://localhost:8080"


def load_glossary_terms():
    """glossary.yml 파일에서 모든 용어들을 로드합니다."""
    glossary_file = "glossary.yml"
    terms = {}

    try:
        with open(glossary_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for node in data.get("nodes", []):
            for term in node.get("terms", []):
                term_name = term.get("name")
                term_description = term.get("description", "")
                terms[term_name] = term_description

        print(f"📚 용어사전에서 {len(terms)}개 용어를 로드했습니다.")
        return terms

    except Exception as e:
        print(f"❌ glossary.yml 로드 중 오류: {e}")
        return {}


def scan_generated_yaml_files():
    """generated_yaml 폴더의 모든 sources.yml 파일을 스캔합니다."""
    yaml_pattern = "../pseudolab/models/generated_yaml/*/sources.yml"
    yaml_files = glob.glob(yaml_pattern)

    datasets = {}

    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            for source in data.get("sources", []):
                source_name = source.get("name")

                for table in source.get("tables", []):
                    table_name = table.get("name")

                    # DataHub URN 형식으로 변환
                    dataset_urn = f"urn:li:dataset:(urn:li:dataPlatform:dbt,{source_name}.{source_name}.{table_name},PROD)"

                    # 각 컬럼 정보 저장
                    columns = []
                    for column in table.get("columns", []):
                        columns.append(
                            {
                                "name": column.get("name"),
                                "description": column.get("description", ""),
                            }
                        )

                    datasets[dataset_urn] = {
                        "source_name": source_name,
                        "table_name": table_name,
                        "columns": columns,
                    }

        except Exception as e:
            print(f"⚠️  {yaml_file} 파일 처리 중 오류: {e}")

    print(f"📁 {len(datasets)}개 데이터셋을 발견했습니다.")
    return datasets


def create_term_matching_rules():
    """용어별 매칭 규칙을 정의합니다."""
    return {
        "고유 식별자": ["식별자", "식별", "ID", "id", "고유"],
        "외래키 참조": ["참조", "외래키", "FK", "fk", "key"],
        "개체명": ["이름", "명칭", "name", "Name"],
        "성명": ["이름", "성명", "name", "Name", "fname", "lname"],
        "별명 및 약어": ["별명", "nickname", "alias", "약어"],
        "위치 정보": ["위치", "장소", "location", "address", "주소"],
        "지역 코드": ["지역", "코드", "code", "region"],
        "날짜 정보": ["날짜", "date", "time", "시간"],
        "설립일": ["설립", "창립", "established", "founded"],
        "방문 시간": ["방문", "visit", "time"],
        "잔액": ["잔액", "balance", "금액"],
        "비용 및 가격": ["비용", "가격", "price", "cost", "fee"],
        "급여": ["급여", "salary", "pay", "wage"],
        "보험 금액": ["보험", "insurance"],
        "나이": ["나이", "age", "연령"],
        "성별": ["성별", "sex", "gender"],
        "신체 정보": ["신체", "키", "몸무게", "height", "weight"],
        "학년": ["학년", "grade", "level"],
        "전공": ["전공", "major", "학과"],
        "지도교수": ["지도교수", "교수", "advisor", "professor"],
        "학생 수": ["학생수", "학생", "student"],
        "소속": ["소속", "기관", "organization"],
        "장르 및 카테고리": ["장르", "카테고리", "genre", "category", "type"],
        "평점 및 평가": ["평점", "평가", "rating", "score"],
        "미디어 파일 정보": ["파일", "미디어", "format"],
        "창작자 정보": ["창작자", "감독", "director", "creator"],
        "시즌 성적": ["시즌", "성적", "season"],
        "승률": ["승률", "승리", "win"],
        "경기장별 성적": ["경기장", "홈", "원정", "home", "away"],
        "거리": ["거리", "distance"],
        "소셜 관계": ["관계", "친구", "friend", "relation"],
        "소유 관계": ["소유", "보유", "has", "own"],
        "분류 관계": ["분류", "카테고리", "class"],
        "시퀀스 관리": ["시퀀스", "sequence", "순서"],
        "API 식별자": ["API", "api"],
        "지불 방법 코드": ["지불", "결제", "payment"],
    }


def match_terms_with_columns(terms, datasets):
    """용어와 컬럼을 매칭하여 TERM_DATASET_MAPPING을 생성합니다."""
    matching_rules = create_term_matching_rules()
    term_dataset_mapping = {}

    print("\n🔍 용어와 컬럼 매칭을 시작합니다...")

    for term_name, term_description in terms.items():
        matching_keywords = matching_rules.get(term_name, [])
        matched_datasets = []

        print(f"\n📋 '{term_name}' 용어 매칭 중...")
        print(f"   키워드: {matching_keywords}")

        for dataset_urn, dataset_info in datasets.items():
            for column in dataset_info["columns"]:
                column_desc = column["description"].lower()
                column_name = column["name"].lower()

                # 키워드 매칭 확인
                for keyword in matching_keywords:
                    if keyword.lower() in column_desc or keyword.lower() in column_name:

                        if dataset_urn not in matched_datasets:
                            matched_datasets.append(dataset_urn)
                            print(
                                f"   ✅ 매칭: {dataset_info['source_name']}.{dataset_info['table_name']}.{column['name']} -> {column['description']}"
                            )
                        break

        if matched_datasets:
            term_dataset_mapping[term_name] = matched_datasets
            print(f"   📊 총 {len(matched_datasets)}개 데이터셋과 매칭됨")
        else:
            print(f"   ⚠️  매칭되는 데이터셋 없음")

    return term_dataset_mapping


def get_glossary_term_urn_by_name(term_name):
    """용어명으로 실제 DataHub URN을 조회합니다."""
    try:
        search_payload = {
            "input": term_name,
            "entity": "glossaryTerm",
            "start": 0,
            "count": 10,
        }

        response = requests.post(
            f"{DATAHUB_GMS_URL}/entities?action=search",
            headers={"Content-Type": "application/json"},
            json=search_payload,
        )

        if response.status_code == 200:
            data = response.json()
            entities = data.get("value", {}).get("entities", [])

            # 정확히 일치하는 용어 찾기
            for entity in entities:
                matched_fields = entity.get("matchedFields", [])
                for field in matched_fields:
                    if field.get("name") == "name" and field.get("value") == term_name:
                        return entity.get("entity")

            # 정확히 일치하는 것이 없으면 첫 번째 결과 반환
            if entities:
                return entities[0].get("entity")

        return None

    except Exception as e:
        print(f"용어 조회 중 오류 발생: {e}")
        return None


def create_glossary_terms_json(term_urn, output_file):
    """용어 적용을 위한 JSON 파일을 생성합니다."""
    aspect_data = {
        "terms": [{"urn": term_urn}],
        "auditStamp": {
            "time": int(time.time() * 1000),  # 현재 시간을 밀리초로
            "actor": "urn:li:corpuser:dwlee",
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(aspect_data, f, indent=2, ensure_ascii=False)


def apply_term_to_dataset(dataset_urn, term_urn, term_name):
    """CLI를 사용해서 용어를 데이터셋에 적용합니다."""
    try:
        # 임시 JSON 파일 생성
        temp_json = "temp_aspect.json"
        create_glossary_terms_json(term_urn, temp_json)

        # CLI 명령어 실행
        cmd = [
            "datahub",
            "put",
            "aspect",
            "--urn",
            dataset_urn,
            "--aspect",
            "glossaryTerms",
            "--aspect-data",
            temp_json,
        ]

        # 환경변수 설정
        env = os.environ.copy()
        env["DATAHUB_GMS_URL"] = DATAHUB_GMS_URL

        result = subprocess.run(cmd, capture_output=True, text=True, env=env)

        # 임시 파일 정리
        if os.path.exists(temp_json):
            os.remove(temp_json)

        if result.returncode == 0:
            print(f"      ✅ 성공: '{term_name}' 용어가 적용되었습니다")
            return True
        else:
            print(f"      ❌ 실패: {result.stderr}")
            return False

    except Exception as e:
        print(f"      ❌ 오류 발생: {e}")
        return False


def main():
    """메인 실행 함수"""
    print("🚀 자동화된 Glossary Terms 적용을 시작합니다...\n")

    # 1. 용어사전 로드
    terms = load_glossary_terms()
    if not terms:
        print("❌ 용어사전 로드 실패. 종료합니다.")
        return

    # 2. 데이터셋 스캔
    datasets = scan_generated_yaml_files()
    if not datasets:
        print("❌ 데이터셋 스캔 실패. 종료합니다.")
        return

    # 3. 용어-컬럼 매칭
    term_dataset_mapping = match_terms_with_columns(terms, datasets)

    if not term_dataset_mapping:
        print("❌ 매칭되는 용어-데이터셋 조합이 없습니다.")
        return

    # 4. DataHub에 적용
    print(f"\n🔧 DataHub에 용어 적용을 시작합니다...")
    success_count = 0
    error_count = 0

    for term_name, dataset_urns in term_dataset_mapping.items():
        print(f"\n📌 용어 '{term_name}' 처리 중...")

        # 용어 URN 조회
        term_urn = get_glossary_term_urn_by_name(term_name)
        if not term_urn:
            print(f"    ⚠️  용어 '{term_name}'의 URN을 찾을 수 없습니다. 건너뜁니다.")
            error_count += len(dataset_urns)
            continue

        print(f"    용어 URN: {term_urn}")

        # 각 데이터셋에 용어 적용
        for dataset_urn in dataset_urns:
            dataset_info = datasets.get(dataset_urn, {})
            dataset_name = f"{dataset_info.get('source_name', '')}.{dataset_info.get('table_name', '')}"
            print(f"    📊 {dataset_name}에 적용 중...")

            if apply_term_to_dataset(dataset_urn, term_urn, term_name):
                success_count += 1
            else:
                error_count += 1

    print("\n" + "=" * 60)
    print(f"🎉 작업 완료!")
    print(f"✅ 성공: {success_count}건")
    print(f"❌ 실패: {error_count}건")
    print(f"📊 총 시도: {success_count + error_count}건")
    print(
        f"📈 성공률: {success_count/(success_count + error_count)*100:.1f}%"
        if (success_count + error_count) > 0
        else "0%"
    )


if __name__ == "__main__":
    main()
