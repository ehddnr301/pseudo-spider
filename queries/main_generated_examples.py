import requests
import json
import os

url = "http://localhost:8080/api/graphql"

headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer <your-token>",  # 필요 시 주석 해제
}

query = """
mutation createQuery($input: CreateQueryInput!) {
  createQuery(input: $input) {
    urn
  }
}
"""


# variables 부분을 외부 파일에서 읽어옴
def load_queries_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# 각 쿼리를 실행하는 함수
def create_query(variables):
    response = requests.post(
        url,
        headers=headers,
        json={"query": query, "variables": variables, "operationName": "createQuery"},
    )
    return response


# 쿼리 데이터 파일 경로
queries_file = "./generated_query_examples.json"

# 파일에서 쿼리 목록 로드
print("📊 Generated YAML 데이터셋 기반 쿼리 예시를 DataHub에 등록합니다...")
queries_data = load_queries_from_file(queries_file)

print(f"총 {len(queries_data)}개의 쿼리를 등록할 예정입니다.")
print("=" * 60)

success_count = 0
error_count = 0

# 각 쿼리에 대해 API 요청 실행
for idx, query_data in enumerate(queries_data):
    query_name = query_data["properties"]["name"]
    print(f"🔍 쿼리 {idx+1}/{len(queries_data)}: '{query_name}' 생성 중...")

    try:
        res = create_query({"input": query_data})

        if res.status_code == 200:
            response_data = res.json()
            if "errors" not in response_data:
                print(
                    f"   ✅ 성공: URN = {response_data.get('data', {}).get('createQuery', {}).get('urn', 'N/A')}"
                )
                success_count += 1
            else:
                print(f"   ❌ 실패: {response_data['errors']}")
                error_count += 1
        else:
            print(f"   ❌ HTTP 오류: 상태 코드 {res.status_code}")
            print(f"   응답: {res.text}")
            error_count += 1

    except Exception as e:
        print(f"   ❌ 예외 발생: {e}")
        error_count += 1

    print("-" * 50)

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
