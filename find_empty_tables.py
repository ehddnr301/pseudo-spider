"""
일곱번째 실행되는 파일
ClickHouse의 모든 데이터베이스에서 빈 테이블(데이터가 없는 테이블)을 찾는 스크립트
"""

import clickhouse_connect
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ClickHouseEmptyTableFinder:
    def __init__(
        self, host="localhost", port=8123, username="clickhouse", password="clickhouse"
    ):
        """
        ClickHouse 연결 초기화

        Args:
            host (str): ClickHouse 호스트
            port (int): ClickHouse 포트
            username (str): 사용자명
            password (str): 비밀번호
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        """ClickHouse에 연결합니다."""
        try:
            self.client = clickhouse_connect.get_client(
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
            )
            return True
        except Exception as e:
            logger.error(f"ClickHouse 연결 실패: {e}")
            return False

    def test_connection(self):
        """
        ClickHouse 연결을 테스트합니다.

        Returns:
            bool: 연결 성공 여부
        """
        try:
            logger.info(f"연결 정보: {self.host}:{self.port} (사용자: {self.username})")

            if not self.client:
                if not self.connect():
                    return False

            # 간단한 쿼리로 연결 테스트
            result = self.client.query("SELECT 1")
            if result and result.result_rows and result.result_rows[0][0] == 1:
                logger.info("ClickHouse 연결 테스트 성공!")
                return True
            else:
                logger.error("ClickHouse 연결 테스트 실패: 예상하지 못한 응답")
                return False

        except Exception as e:
            logger.error(f"ClickHouse 연결 테스트 실패: {e}")
            logger.error(f"연결 정보를 확인해주세요:")
            logger.error(f"  - 호스트: {self.host}")
            logger.error(f"  - 포트: {self.port}")
            logger.error(f"  - 사용자명: {self.username}")
            logger.error(f"  - ClickHouse 서버가 실행 중인지 확인해주세요")
            return False

    def get_all_databases(self):
        """
        모든 데이터베이스 목록을 조회합니다.
        시스템 데이터베이스는 제외합니다.

        Returns:
            list: 데이터베이스 이름 리스트
        """
        query = """
        SELECT name 
        FROM system.databases 
        WHERE name NOT IN ('system', 'information_schema', 'INFORMATION_SCHEMA')
        ORDER BY name
        """

        try:
            result = self.client.query(query)
            databases = [row[0] for row in result.result_rows]
            logger.info(f"발견된 데이터베이스: {databases}")
            return databases
        except Exception as e:
            logger.error(f"데이터베이스 조회 중 오류 발생: {e}")
            return []

    def get_tables_in_database(self, database):
        """
        특정 데이터베이스의 모든 테이블을 조회합니다.

        Args:
            database (str): 데이터베이스 이름

        Returns:
            list: 테이블 이름 리스트
        """
        query = f"""
        SELECT name 
        FROM system.tables 
        WHERE database = '{database}'
        ORDER BY name
        """

        try:
            result = self.client.query(query)
            tables = [row[0] for row in result.result_rows]
            logger.info(f"데이터베이스 '{database}'에서 발견된 테이블: {len(tables)}개")
            return tables
        except Exception as e:
            logger.error(f"데이터베이스 '{database}'의 테이블 조회 중 오류 발생: {e}")
            return []

    def get_table_row_count(self, database, table):
        """
        특정 테이블의 행 수를 조회합니다.

        Args:
            database (str): 데이터베이스 이름
            table (str): 테이블 이름

        Returns:
            int: 테이블의 행 수
        """
        query = f"SELECT count() FROM `{database}`.`{table}`"

        try:
            result = self.client.query(query)
            row_count = result.result_rows[0][0]
            return row_count
        except Exception as e:
            logger.error(f"테이블 '{database}.{table}'의 행 수 조회 중 오류 발생: {e}")
            return -1  # 오류 발생시 -1 반환

    def find_empty_tables(self):
        """
        모든 데이터베이스에서 빈 테이블을 찾습니다.

        Returns:
            tuple: (빈 테이블 정보 리스트, 모든 테이블 정보 리스트)
        """
        empty_tables = []
        all_tables_info = []

        databases = self.get_all_databases()

        if not databases:
            logger.warning("조회할 데이터베이스가 없습니다.")
            return empty_tables, all_tables_info  # 빈 리스트 두 개 반환

        for database in databases:
            logger.info(f"\n데이터베이스 '{database}' 조회 중...")
            tables = self.get_tables_in_database(database)

            if not tables:
                logger.info(f"데이터베이스 '{database}'에 테이블이 없습니다.")
                continue

            for table in tables:
                row_count = self.get_table_row_count(database, table)

                table_info = {
                    "database": database,
                    "table": table,
                    "row_count": row_count,
                }
                all_tables_info.append(table_info)

                if row_count == 0:
                    empty_tables.append(table_info)
                    logger.info(f"  ✓ 빈 테이블 발견: {database}.{table}")
                elif row_count < 0:
                    logger.warning(f"  ⚠ 조회 실패: {database}.{table}")
                # 데이터가 있는 테이블은 로그 출력하지 않음

        return empty_tables, all_tables_info

    def print_summary(self, empty_tables, all_tables_info):
        """
        빈 테이블 조회 결과를 출력합니다.

        Args:
            empty_tables (list): 빈 테이블 리스트
            all_tables_info (list): 모든 테이블 정보 리스트
        """
        print("\n" + "=" * 60)
        print("🗂️ ClickHouse 빈 테이블 조회 결과")
        print("=" * 60)

        print(f"총 테이블 수: {len(all_tables_info)}개")
        print(f"빈 테이블 수: {len(empty_tables)}개")

        if empty_tables:
            print(f"\n📋 빈 테이블 목록 ({len(empty_tables)}개):")
            for i, table_info in enumerate(empty_tables, 1):
                print(f"  {i:2d}. {table_info['database']}.{table_info['table']}")
        else:
            print("\n✅ 모든 테이블에 데이터가 있습니다!")

        print("=" * 60)

    def close(self):
        """클라이언트 연결을 종료합니다."""
        try:
            if self.client:
                self.client.close()
                logger.info("ClickHouse 연결이 종료되었습니다.")
        except:
            pass


def main():
    """메인 함수"""
    # ClickHouse 연결 정보
    clickhouse_host = "127.0.0.1"
    clickhouse_port = 8123
    clickhouse_username = "clickhouse"
    clickhouse_password = "clickhouse"

    finder = None

    try:
        # ClickHouse 연결
        print("🔌 ClickHouse에 연결 중...")
        finder = ClickHouseEmptyTableFinder(
            host=clickhouse_host,
            port=clickhouse_port,
            username=clickhouse_username,
            password=clickhouse_password,
        )

        # 연결 테스트
        if not finder.test_connection():
            print(f"\n❌ 오류 발생: ClickHouse 연결 테스트 실패")
            return []

        print("✅ ClickHouse 연결 성공!")

        # 빈 테이블 찾기
        print("\n🔍 빈 테이블 검색 시작...")
        empty_tables, all_tables_info = finder.find_empty_tables()

        # 결과 출력
        finder.print_summary(empty_tables, all_tables_info)

        # 빈 테이블 리스트 반환 (다른 스크립트에서 import할 경우 사용)
        return empty_tables

    except Exception as e:
        logger.error(f"실행 중 오류 발생: {e}")
        print(f"\n❌ 오류 발생: {e}")
        return []

    finally:
        if finder:
            finder.close()


if __name__ == "__main__":
    main()
