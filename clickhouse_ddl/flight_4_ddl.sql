-- ClickHouse DDL for database: flight_4
-- Generated from: spider_data/database/flight_4/flight_4.sqlite

CREATE DATABASE IF NOT EXISTS flight_4;

CREATE TABLE `flight_4`.`routes` (
    `rid` Int64,
    `dst_apid` Nullable(Int64),
    `dst_ap` Nullable(String),
    `src_apid` Nullable(Int64),
    `src_ap` Nullable(String),
    `alid` Nullable(Int64),
    `airline` Nullable(String),
    `codeshare` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `rid`;

CREATE TABLE `flight_4`.`airports` (
    `apid` Int64,
    `name` String,
    `city` Nullable(String),
    `country` Nullable(String),
    `x` Nullable(Float64),
    `y` Nullable(Float64),
    `elevation` Nullable(Int64),
    `iata` Nullable(String),
    `icao` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `apid`;

CREATE TABLE `flight_4`.`airlines` (
    `alid` Int64,
    `name` Nullable(String),
    `iata` Nullable(String),
    `icao` Nullable(String),
    `callsign` Nullable(String),
    `country` Nullable(String),
    `active` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `alid`;

