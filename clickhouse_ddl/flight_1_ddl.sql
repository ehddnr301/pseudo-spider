-- ClickHouse DDL for database: flight_1
-- Generated from: spider_data/database/flight_1/flight_1.sqlite

CREATE DATABASE IF NOT EXISTS flight_1;

CREATE TABLE `flight_1`.`flight` (
    `flno` String,
    `origin` Nullable(String),
    `destination` Nullable(String),
    `distance` Nullable(String),
    `departure_date` Nullable(Date),
    `arrival_date` Nullable(Date),
    `price` Nullable(String),
    `aid` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `flno`;

CREATE TABLE `flight_1`.`aircraft` (
    `aid` String,
    `name` Nullable(String),
    `distance` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `aid`;

CREATE TABLE `flight_1`.`employee` (
    `eid` String,
    `name` Nullable(String),
    `salary` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `eid`;

CREATE TABLE `flight_1`.`certificate` (
    `eid` String,
    `aid` String
)
ENGINE = MergeTree()
ORDER BY (`eid`, `aid`);

