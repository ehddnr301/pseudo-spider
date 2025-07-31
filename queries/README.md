# DataHub 쿼리 생성 및 관리 도구

이 디렉토리는 DataHub에 등록된 데이터셋들에 대한 다양한 쿼리 예시를 생성하고 관리하는 도구들을 포함하고 있습니다.

## 📁 파일 구조

```
queries/
├── README.md                      # 이 문서
├── main.py                        # 기본 쿼리 실행 스크립트
├── main_generated_examples.py     # 생성된 예시 쿼리 실행 스크립트
├── auto_generate_queries.py       # 자동 쿼리 생성 스크립트
├── query_data.json               # 수동으로 작성된 쿼리 예시
├── generated_query_examples.json # 큐레이션된 고품질 쿼리 예시
└── auto_generated_queries.json   # 자동 생성된 쿼리들 (실행 후 생성됨)
```

## 🚀 사용법

### 1. 자동 쿼리 생성

`generated_yaml` 폴더의 모든 데이터셋을 스캔하여 자동으로 기본 분석 쿼리들을 생성합니다.

```bash
cd queries
python auto_generate_queries.py
```

**생성되는 쿼리 타입:**
- 전체 데이터 수 조회
- 컬럼별 데이터 분포 분석
- 숫자/평점 컬럼 통계 분석 
- 날짜 기반 트렌드 분석
- 상위 랭킹 분석

### 2. 큐레이션된 예시 쿼리 실행

수동으로 작성된 고품질의 비즈니스 쿼리들을 DataHub에 등록합니다.

```bash
python main_generated_examples.py
```

**포함된 도메인:**
- 🎓 교육 (학생, 교사)
- 🍽️ 레스토랑 (방문, 선호도)
- 🎵 음악 (아티스트, 장르)
- ✈️ 항공 (비행편, 가격)
- 🛍️ 쇼핑몰 (회원, 매출)
- ⚽ 스포츠 (축구, 선수)
- 🎬 영화 (평점, 감독)
- 🏦 금융 (은행, 계좌)

### 3. 기본 쿼리 실행

기존의 수동 작성 쿼리를 실행합니다.

```bash
python main.py
```

## 📊 쿼리 형식

모든 쿼리는 DataHub의 Query 엔티티 형식을 따릅니다:

```json
{
  "properties": {
    "name": "쿼리 이름",
    "description": "쿼리 설명",
    "statement": {
      "value": "SELECT * FROM table;",
      "language": "SQL"
    }
  },
  "subjects": [
    {
      "datasetUrn": "urn:li:dataset:(urn:li:dataPlatform:dbt,source.source.table,PROD)"
    }
  ]
}
```

## 🔧 설정

### DataHub 연결 설정

`main.py` 및 관련 스크립트에서 DataHub 서버 URL을 확인하세요:

```python
url = "http://localhost:8080/api/graphql"
```

### 필요한 패키지

```bash
pip install requests pyyaml
```

## 💡 쿼리 작성 가이드라인

### 좋은 쿼리 예시:
- **명확한 비즈니스 목적**: "학년별 학생 수 분석"
- **구체적인 설명**: "각 학년별 학생 수를 집계하여 학교의 학년별 인구 분포를 파악"
- **실행 가능한 SQL**: 실제 데이터 구조에 맞는 유효한 쿼리
- **적절한 범위**: 너무 복잡하지 않고 명확한 결과를 제공

### 피해야 할 것:
- 모호한 목적의 쿼리
- 데이터 구조와 맞지 않는 SQL
- 과도하게 복잡한 조인이나 서브쿼리
- 성능에 영향을 줄 수 있는 전체 테이블 스캔

## 🎯 확장 방법

### 새로운 쿼리 타입 추가

`auto_generate_queries.py`에서 새로운 쿼리 생성 함수를 추가할 수 있습니다:

```python
def generate_custom_queries(dataset_urn, dataset_info, column_types):
    """커스텀 쿼리 생성 로직"""
    queries = []
    # 쿼리 생성 로직 구현
    return queries
```

### 새로운 도메인 추가

`generated_query_examples.json`에 새로운 도메인의 쿼리들을 수동으로 추가할 수 있습니다.

## 🐛 트러블슈팅

### 자주 발생하는 문제:

1. **DataHub 연결 실패**
   - DataHub 서버가 실행 중인지 확인
   - URL과 포트가 올바른지 확인

2. **쿼리 생성 실패**
   - `generated_yaml` 폴더 경로가 올바른지 확인
   - YAML 파일 형식이 올바른지 확인

3. **SQL 구문 오류**
   - 생성된 쿼리의 SQL이 실제 스키마와 일치하는지 확인
   - 컬럼명과 테이블명이 정확한지 확인

## 📈 성과 지표

쿼리 실행 후 다음과 같은 통계가 표시됩니다:
- ✅ 성공한 쿼리 수
- ❌ 실패한 쿼리 수  
- 📊 전체 시도 횟수
- 📈 성공률

이를 통해 데이터 품질과 쿼리 유효성을 모니터링할 수 있습니다. 