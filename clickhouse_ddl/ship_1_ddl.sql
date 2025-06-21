-- ClickHouse DDL for database: ship_1
-- Generated from: spider_data/database/ship_1/ship_1.sqlite

CREATE DATABASE IF NOT EXISTS ship_1;

CREATE TABLE `ship_1`.`captain` (
    `Captain_ID` Int32,
    `Name` Nullable(String),
    `Ship_ID` Nullable(Int32),
    `age` Nullable(String),
    `Class` Nullable(String),
    `Rank` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Captain_ID`;

CREATE TABLE `ship_1`.`Ship` (
    `Ship_ID` Int32,
    `Name` Nullable(String),
    `Type` Nullable(String),
    `Built_Year` Nullable(Float64),
    `Class` Nullable(String),
    `Flag` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Ship_ID`;

