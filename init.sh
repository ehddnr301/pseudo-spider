#!/bin/bash

# spider_data 디렉토리 존재 여부 확인
if [ ! -d "spider_data" ]; then
    echo "오류: spider_data 디렉토리가 존재하지 않습니다."
    echo "spider_data 디렉토리를 먼저 생성해주세요."
    exit 1
fi

echo "spider_data 디렉토리 확인 완료"

echo "첫번째"

python create_database.py

echo "두번째"

python create_ddl.py

echo "세번째"

python execute_ddl.py

echo "네번째"

python generate_fake_data.py

echo "다섯번째"

python remove_unnecessary.py

echo "여섯번째"

python data_inserter.py

echo "일곱번째"

python find_empty_tables.py

echo "여덟번째"

python generate_fake_yaml.py

echo "아홉번째"

python remove_tests_from_yaml.py