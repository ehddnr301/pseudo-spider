"""
여섯번째 실행되는 파일
temp_faker_code 디렉토리 하위의 모든 모듈을 실행하고 데이터를 ClickHouse에 삽입
"""

import os
import importlib.util
import clickhouse_connect
from typing import List, Dict, Any
import logging
import pandas as pd
from clickhouse_connect.driver.query import QueryContext

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_inserter.log", encoding="utf-8"),
        logging.StreamHandler(),  # 콘솔 출력도 유지
    ],
)
logger = logging.getLogger(__name__)

# ClickHouse 연결 설정
CLICKHOUSE_CONFIG = {
    "host": "localhost",
    "port": 8124,
    "username": "clickhouse",
    "password": "clickhouse",
    "database": "default",
}


def get_faker_modules() -> List[Dict[str, str]]:
    """temp_faker_code 디렉토리에서 모든 faker 모듈을 찾습니다."""
    faker_dir = "temp_faker_code"
    modules = []

    for db_name in os.listdir(faker_dir):
        db_path = os.path.join(faker_dir, db_name)
        if os.path.isdir(db_path):
            for file in os.listdir(db_path):
                if file.endswith(".py") and file.startswith("temp_faker_"):
                    modules.append(
                        {
                            "db_name": db_name,
                            "module_path": os.path.join(db_path, file),
                            "module_name": file.replace(".py", ""),
                        }
                    )
    return modules


def import_module(module_path: str) -> Any:
    """모듈을 동적으로 import 합니다."""
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def execute_faker_and_insert(
    client: Any,
    module_info: Dict[str, str],
    num_records: int = 100,
) -> None:
    """faker 모듈을 실행하고 데이터를 ClickHouse에 삽입합니다."""
    try:
        module = import_module(module_info["module_path"])
        db_name = module_info["db_name"]
        table_name = module_info["module_name"].replace("temp_faker_", "")

        # 모듈의 main 함수 실행
        if hasattr(module, "generate_fake_data"):
            data = module.generate_fake_data(num_records)
            if data:
                # 데이터를 DataFrame으로 변환
                df = pd.DataFrame(data)

                # CSV로 저장
                csv_path = f"generated_data/{db_name}/{table_name}.csv"
                os.makedirs(os.path.dirname(csv_path), exist_ok=True)
                df.to_csv(csv_path, index=False, encoding="utf-8")

                # ClickHouse에 데이터 삽입
                if not df.empty:
                    # DataFrame을 ClickHouse에 삽입
                    client.insert_df(
                        f"{db_name}.{table_name}", df, column_names=df.columns.tolist()
                    )
                    logger.info(
                        f"Successfully inserted {len(df)} records into {db_name}.{table_name}"
                    )
                else:
                    logger.warning(f"No data to insert into {db_name}.{table_name}")
            else:
                logger.warning(f"No data generated from {module_info['module_name']}")
        else:
            logger.warning(f"No main function found in {module_info['module_name']}")

    except Exception as e:
        logger.error(f"Error processing {module_info['module_path']}: {str(e)}")


def main():
    """메인 실행 함수"""
    try:
        # ClickHouse 클라이언트 연결
        client = clickhouse_connect.get_client(**CLICKHOUSE_CONFIG)
        logger.info("Connected to ClickHouse")

        # 모든 faker 모듈 실행 (현재는 주석 처리)
        for module_info in get_faker_modules():
            execute_faker_and_insert(client, module_info)
        logger.info("All data insertion completed")

        # 특정 모듈만 실행
        # module_info = {
        #     "db_name": "world_1",
        #     "module_path": "temp_faker_code/world_1/temp_faker_city.py",
        #     "module_name": "temp_faker_city",
        # }
        # execute_faker_and_insert(client, module_info)

        logger.info("Data insertion completed")

    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
    finally:
        if "client" in locals():
            client.close()


if __name__ == "__main__":
    main()
