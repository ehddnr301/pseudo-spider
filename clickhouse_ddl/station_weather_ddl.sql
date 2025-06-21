-- ClickHouse DDL for database: station_weather
-- Generated from: spider_data/database/station_weather/station_weather.sqlite

CREATE DATABASE IF NOT EXISTS station_weather;

CREATE TABLE `station_weather`.`train` (
    `id` Int32,
    `train_number` Nullable(Int32),
    `name` Nullable(String),
    `origin` Nullable(String),
    `destination` Nullable(String),
    `time` Nullable(String),
    `interval` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `station_weather`.`station` (
    `id` Int32,
    `network_name` Nullable(String),
    `services` Nullable(String),
    `local_authority` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `station_weather`.`route` (
    `train_id` Int32,
    `station_id` Int32
)
ENGINE = MergeTree()
ORDER BY (`train_id`, `station_id`);

CREATE TABLE `station_weather`.`weekly_weather` (
    `station_id` Int32,
    `day_of_week` String,
    `high_temperature` Nullable(Int32),
    `low_temperature` Nullable(Int32),
    `precipitation` Nullable(Float64),
    `wind_speed_mph` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`station_id`, `day_of_week`);

