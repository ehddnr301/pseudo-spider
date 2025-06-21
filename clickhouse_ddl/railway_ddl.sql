-- ClickHouse DDL for database: railway
-- Generated from: spider_data/database/railway/railway.sqlite

CREATE DATABASE IF NOT EXISTS railway;

CREATE TABLE `railway`.`railway` (
    `Railway_ID` Int32,
    `Railway` Nullable(String),
    `Builder` Nullable(String),
    `Built` Nullable(String),
    `Wheels` Nullable(String),
    `Location` Nullable(String),
    `ObjectNumber` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Railway_ID`;

CREATE TABLE `railway`.`train` (
    `Train_ID` Int32,
    `Train_Num` Nullable(String),
    `Name` Nullable(String),
    `From` Nullable(String),
    `Arrival` Nullable(String),
    `Railway_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Train_ID`;

CREATE TABLE `railway`.`manager` (
    `Manager_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `Working_year_starts` Nullable(String),
    `Age` Nullable(Int32),
    `Level` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Manager_ID`;

CREATE TABLE `railway`.`railway_manage` (
    `Railway_ID` Int32,
    `Manager_ID` Int32,
    `From_Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Railway_ID`, `Manager_ID`);

