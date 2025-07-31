#!/usr/bin/env python3

import yaml
import json
import glob
import random
from pathlib import Path


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
                        "table_description": table.get("description", ""),
                        "columns": columns,
                    }

        except Exception as e:
            print(f"⚠️  {yaml_file} 파일 처리 중 오류: {e}")

    print(f"📁 {len(datasets)}개 데이터셋을 발견했습니다.")
    return datasets


def identify_column_types(columns):
    """컬럼명과 설명을 기반으로 컬럼 타입을 분류합니다."""
    id_columns = []
    name_columns = []
    date_columns = []
    numeric_columns = []
    rating_columns = []
    location_columns = []

    for col in columns:
        col_name = col["name"].lower()
        col_desc = col["description"].lower()

        # ID 컬럼
        if "id" in col_name or "식별자" in col_desc or "고유" in col_desc:
            id_columns.append(col["name"])

        # 이름 관련 컬럼
        elif "name" in col_name or "이름" in col_desc or "명칭" in col_desc:
            name_columns.append(col["name"])

        # 날짜 관련 컬럼
        elif any(word in col_name for word in ["date", "time", "year"]) or any(
            word in col_desc for word in ["날짜", "시간", "연도"]
        ):
            date_columns.append(col["name"])

        # 평점 관련 컬럼
        elif any(word in col_name for word in ["rating", "score", "stars"]) or any(
            word in col_desc for word in ["평점", "점수", "별점"]
        ):
            rating_columns.append(col["name"])

        # 위치 관련 컬럼
        elif any(
            word in col_name for word in ["address", "city", "country", "location"]
        ) or any(word in col_desc for word in ["주소", "도시", "국가", "위치"]):
            location_columns.append(col["name"])

        # 숫자 관련 컬럼 (가격, 급여, 잔액 등)
        elif any(
            word in col_name
            for word in ["price", "salary", "balance", "amount", "cost", "spent"]
        ) or any(word in col_desc for word in ["가격", "급여", "잔액", "금액", "비용"]):
            numeric_columns.append(col["name"])

    return {
        "id_columns": id_columns,
        "name_columns": name_columns,
        "date_columns": date_columns,
        "numeric_columns": numeric_columns,
        "rating_columns": rating_columns,
        "location_columns": location_columns,
    }


def generate_basic_queries(dataset_urn, dataset_info):
    """기본적인 데이터 탐색 쿼리들을 생성합니다."""
    queries = []
    source_name = dataset_info["source_name"]
    table_name = dataset_info["table_name"]
    table_description = dataset_info["table_description"]

    # 전체 데이터 수 조회
    queries.append(
        {
            "properties": {
                "name": f"{table_name} 테이블 전체 데이터 수 조회",
                "description": f"{table_description}의 전체 레코드 수를 확인하여 데이터 규모 파악",
                "statement": {
                    "value": f"SELECT COUNT(*) as total_count FROM dbt.{source_name}.{source_name}.{table_name};",
                    "language": "SQL",
                },
            },
            "subjects": [{"datasetUrn": dataset_urn}],
        }
    )

    return queries


def generate_aggregation_queries(dataset_urn, dataset_info, column_types):
    """집계 쿼리들을 생성합니다."""
    queries = []
    source_name = dataset_info["source_name"]
    table_name = dataset_info["table_name"]

    # 그룹별 집계 쿼리
    for col in column_types["name_columns"] + column_types["location_columns"]:
        if col:
            queries.append(
                {
                    "properties": {
                        "name": f"{col}별 데이터 분포 분석",
                        "description": f"{table_name} 테이블에서 {col}별 데이터 수를 집계하여 분포 현황 파악",
                        "statement": {
                            "value": f"SELECT {col}, COUNT(*) as count FROM dbt.{source_name}.{source_name}.{table_name} GROUP BY {col} ORDER BY count DESC LIMIT 10;",
                            "language": "SQL",
                        },
                    },
                    "subjects": [{"datasetUrn": dataset_urn}],
                }
            )

    # 숫자 컬럼 통계
    for col in column_types["numeric_columns"] + column_types["rating_columns"]:
        if col:
            queries.append(
                {
                    "properties": {
                        "name": f"{col} 통계 분석",
                        "description": f"{table_name} 테이블의 {col} 값에 대한 기본 통계(평균, 최대, 최소값) 분석",
                        "statement": {
                            "value": f"SELECT AVG({col}) as avg_value, MIN({col}) as min_value, MAX({col}) as max_value, COUNT(*) as total_count FROM dbt.{source_name}.{source_name}.{table_name} WHERE {col} IS NOT NULL;",
                            "language": "SQL",
                        },
                    },
                    "subjects": [{"datasetUrn": dataset_urn}],
                }
            )

    return queries


def generate_temporal_queries(dataset_urn, dataset_info, column_types):
    """시간 기반 쿼리들을 생성합니다."""
    queries = []
    source_name = dataset_info["source_name"]
    table_name = dataset_info["table_name"]

    for date_col in column_types["date_columns"]:
        if date_col:
            # 연도별 트렌드
            if "year" in date_col.lower() or "연도" in date_col.lower():
                queries.append(
                    {
                        "properties": {
                            "name": f"{date_col}별 데이터 트렌드 분석",
                            "description": f"{table_name} 테이블의 {date_col}별 데이터 변화 추세를 분석",
                            "statement": {
                                "value": f"SELECT {date_col}, COUNT(*) as count FROM dbt.{source_name}.{source_name}.{table_name} WHERE {date_col} IS NOT NULL GROUP BY {date_col} ORDER BY {date_col} DESC;",
                                "language": "SQL",
                            },
                        },
                        "subjects": [{"datasetUrn": dataset_urn}],
                    }
                )
            else:
                # 날짜별 트렌드 (년도 추출)
                queries.append(
                    {
                        "properties": {
                            "name": f"{date_col} 기반 연도별 트렌드 분석",
                            "description": f"{table_name} 테이블의 {date_col}에서 연도를 추출하여 연도별 데이터 트렌드 분석",
                            "statement": {
                                "value": f"SELECT YEAR({date_col}) as year, COUNT(*) as count FROM dbt.{source_name}.{source_name}.{table_name} WHERE {date_col} IS NOT NULL GROUP BY YEAR({date_col}) ORDER BY year DESC;",
                                "language": "SQL",
                            },
                        },
                        "subjects": [{"datasetUrn": dataset_urn}],
                    }
                )

    return queries


def generate_top_bottom_queries(dataset_urn, dataset_info, column_types):
    """상위/하위 랭킹 쿼리들을 생성합니다."""
    queries = []
    source_name = dataset_info["source_name"]
    table_name = dataset_info["table_name"]

    # 평점이나 숫자 값 기준 상위/하위
    ranking_cols = column_types["rating_columns"] + column_types["numeric_columns"]
    name_cols = column_types["name_columns"]

    if ranking_cols and name_cols:
        ranking_col = ranking_cols[0]
        name_col = name_cols[0]

        queries.append(
            {
                "properties": {
                    "name": f"{ranking_col} 기준 상위 항목 분석",
                    "description": f"{table_name} 테이블에서 {ranking_col} 값이 높은 상위 항목들을 조회",
                    "statement": {
                        "value": f"SELECT {name_col}, {ranking_col} FROM dbt.{source_name}.{source_name}.{table_name} WHERE {ranking_col} IS NOT NULL ORDER BY {ranking_col} DESC LIMIT 10;",
                        "language": "SQL",
                    },
                },
                "subjects": [{"datasetUrn": dataset_urn}],
            }
        )

    return queries


def generate_all_queries():
    """모든 데이터셋에 대해 자동으로 쿼리를 생성합니다."""
    print("🚀 자동 쿼리 생성을 시작합니다...\n")

    # 데이터셋 스캔
    datasets = scan_generated_yaml_files()

    all_queries = []

    for dataset_urn, dataset_info in datasets.items():
        print(
            f"📊 {dataset_info['source_name']}.{dataset_info['table_name']} 처리 중..."
        )

        # 컬럼 타입 분류
        column_types = identify_column_types(dataset_info["columns"])

        # 다양한 타입의 쿼리 생성
        queries = []
        queries.extend(generate_basic_queries(dataset_urn, dataset_info))
        queries.extend(
            generate_aggregation_queries(dataset_urn, dataset_info, column_types)
        )
        queries.extend(
            generate_temporal_queries(dataset_urn, dataset_info, column_types)
        )
        queries.extend(
            generate_top_bottom_queries(dataset_urn, dataset_info, column_types)
        )

        # 랜덤하게 일부 쿼리만 선택 (너무 많아지지 않도록)
        if len(queries) > 3:
            queries = random.sample(queries, min(3, len(queries)))

        all_queries.extend(queries)
        print(f"   ✅ {len(queries)}개 쿼리 생성됨")

    # JSON 파일로 저장
    output_file = "auto_generated_queries.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_queries, f, indent=2, ensure_ascii=False)

    print(
        f"\n🎉 총 {len(all_queries)}개의 쿼리가 생성되어 '{output_file}' 파일에 저장되었습니다!"
    )
    return all_queries


if __name__ == "__main__":
    generate_all_queries()
