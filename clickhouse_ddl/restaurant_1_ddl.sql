-- ClickHouse DDL for database: restaurant_1
-- Generated from: spider_data/database/restaurant_1/restaurant_1.sqlite

CREATE DATABASE IF NOT EXISTS restaurant_1;

CREATE TABLE `restaurant_1`.`Student` (
    `StuID` Int64,
    `LName` Nullable(String),
    `Fname` Nullable(String),
    `Age` Nullable(Int64),
    `Sex` Nullable(String),
    `Major` Nullable(Int64),
    `Advisor` Nullable(Int64),
    `city_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `StuID`;

CREATE TABLE `restaurant_1`.`Restaurant` (
    `ResID` Int64,
    `ResName` Nullable(String),
    `Address` Nullable(String),
    `Rating` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `ResID`;

CREATE TABLE `restaurant_1`.`Type_Of_Restaurant` (
    `ResID` Nullable(Int64),
    `ResTypeID` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `restaurant_1`.`Restaurant_Type` (
    `ResTypeID` Int64,
    `ResTypeName` Nullable(String),
    `ResTypeDescription` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ResTypeID`;

CREATE TABLE `restaurant_1`.`Visits_Restaurant` (
    `StuID` Nullable(Int64),
    `ResID` Nullable(Int64),
    `Time` Nullable(DateTime),
    `Spent` Nullable(Float32)
)
ENGINE = MergeTree()
ORDER BY tuple();

