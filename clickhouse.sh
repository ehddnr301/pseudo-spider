docker run -d \
  --name clickhouse2 \
  --ulimit nofile=262144:262144 \
  -p 8124:8123 \
  -p 9001:9000 \
  -p 9004:9009 \
  -e CLICKHOUSE_USER=clickhouse \
  -e CLICKHOUSE_PASSWORD=clickhouse \
  -e CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT=1 \
  clickhouse/clickhouse-server
