# Pseudo Spider

## 시작하기

### 설치 및 실행

1. 저장소 클론
```bash
git clone https://github.com/ehddnr301/pseudo-spider
cd pseudo-spider
```

2. 도커 컨테이너 실행
```bash
docker compose up -d
```

## 알려진 이슈

- 간헐적으로 에러가 발생할 수 있습니다. 이 경우 다음 단계를 시도해보세요:
  - 문제가 지속되면 전체 재시작: `docker compose down && docker compose up -d`

## 프로젝트 구조

```
pseudo-spider/
├── docker-compose.yml    # 도커 컴포즈 설정
└── ...                   # 기타 프로젝트 파일들
```

## 데이터 생성

- spider dataset을 받아서 init.sh 로 생성했는데 신경쓰실 필요는 없습니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
