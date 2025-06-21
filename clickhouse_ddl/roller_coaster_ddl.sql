-- ClickHouse DDL for database: roller_coaster
-- Generated from: spider_data/database/roller_coaster/roller_coaster.sqlite

CREATE DATABASE IF NOT EXISTS roller_coaster;

CREATE TABLE `roller_coaster`.`roller_coaster` (
    `Roller_Coaster_ID` Int32,
    `Name` Nullable(String),
    `Park` Nullable(String),
    `Country_ID` Nullable(Int32),
    `Length` Nullable(Float64),
    `Height` Nullable(Float64),
    `Speed` Nullable(String),
    `Opened` Nullable(String),
    `Status` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Roller_Coaster_ID`;

CREATE TABLE `roller_coaster`.`country` (
    `Country_ID` Int32,
    `Name` Nullable(String),
    `Population` Nullable(Int32),
    `Area` Nullable(Int32),
    `Languages` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Country_ID`;

