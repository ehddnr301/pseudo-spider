-- ClickHouse DDL for database: swimming
-- Generated from: spider_data/database/swimming/swimming.sqlite

CREATE DATABASE IF NOT EXISTS swimming;

CREATE TABLE `swimming`.`swimmer` (
    `ID` Int32,
    `name` Nullable(String),
    `Nationality` Nullable(String),
    `meter_100` Nullable(Float64),
    `meter_200` Nullable(String),
    `meter_300` Nullable(String),
    `meter_400` Nullable(String),
    `meter_500` Nullable(String),
    `meter_600` Nullable(String),
    `meter_700` Nullable(String),
    `Time` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `swimming`.`stadium` (
    `ID` Int32,
    `name` Nullable(String),
    `Capacity` Nullable(Int32),
    `City` Nullable(String),
    `Country` Nullable(String),
    `Opening_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `swimming`.`event` (
    `ID` Int32,
    `Name` Nullable(String),
    `Stadium_ID` Nullable(Int32),
    `Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `swimming`.`record` (
    `ID` Nullable(Int32),
    `Result` Nullable(String),
    `Swimmer_ID` Int32,
    `Event_ID` Int32
)
ENGINE = MergeTree()
ORDER BY (`Swimmer_ID`, `Event_ID`);

