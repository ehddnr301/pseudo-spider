#!/bin/bash

# datahub 시작
datahub docker quickstart

# datahub가 준비될 때까지 대기
until curl -s http://localhost:9002/health; do
    echo "Waiting for datahub to be ready..."
    sleep 10
done

# dbt docs 생성
cd "$(pwd)/pseudolab"
dbt docs generate --profiles-dir "$(pwd)/pseudolab/profiles"

# datahub에 메타데이터 수집
datahub ingest -c "$(pwd)/recipe.yml"

# 컨테이너가 계속 실행되도록 유지
tail -f /dev/null