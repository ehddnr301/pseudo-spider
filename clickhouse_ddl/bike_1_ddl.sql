-- ClickHouse DDL for database: bike_1
-- Generated from: spider_data/database/bike_1/bike_1.sqlite

CREATE DATABASE IF NOT EXISTS bike_1;

CREATE TABLE `bike_1`.`station` (
    `id` Int64,
    `name` Nullable(String),
    `lat` Nullable(Decimal64(2)),
    `long` Nullable(Decimal64(2)),
    `dock_count` Nullable(Int64),
    `city` Nullable(String),
    `installation_date` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `bike_1`.`status` (
    `station_id` Nullable(Int64),
    `bikes_available` Nullable(Int64),
    `docks_available` Nullable(Int64),
    `time` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `bike_1`.`trip` (
    `id` Int64,
    `duration` Nullable(Int64),
    `start_date` Nullable(String),
    `start_station_name` Nullable(String),
    `start_station_id` Nullable(Int64),
    `end_date` Nullable(String),
    `end_station_name` Nullable(String),
    `end_station_id` Nullable(Int64),
    `bike_id` Nullable(Int64),
    `subscription_type` Nullable(String),
    `zip_code` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `bike_1`.`weather` (
    `date` Nullable(String),
    `max_temperature_f` Nullable(Int64),
    `mean_temperature_f` Nullable(Int64),
    `min_temperature_f` Nullable(Int64),
    `max_dew_point_f` Nullable(Int64),
    `mean_dew_point_f` Nullable(Int64),
    `min_dew_point_f` Nullable(Int64),
    `max_humidity` Nullable(Int64),
    `mean_humidity` Nullable(Int64),
    `min_humidity` Nullable(Int64),
    `max_sea_level_pressure_inches` Nullable(Decimal64(2)),
    `mean_sea_level_pressure_inches` Nullable(Decimal64(2)),
    `min_sea_level_pressure_inches` Nullable(Decimal64(2)),
    `max_visibility_miles` Nullable(Int64),
    `mean_visibility_miles` Nullable(Int64),
    `min_visibility_miles` Nullable(Int64),
    `max_wind_Speed_mph` Nullable(Int64),
    `mean_wind_speed_mph` Nullable(Int64),
    `max_gust_speed_mph` Nullable(Int64),
    `precipitation_inches` Nullable(Int64),
    `cloud_cover` Nullable(Int64),
    `events` Nullable(String),
    `wind_dir_degrees` Nullable(Int64),
    `zip_code` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

