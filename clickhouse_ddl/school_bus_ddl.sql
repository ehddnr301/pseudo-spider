-- ClickHouse DDL for database: school_bus
-- Generated from: spider_data/database/school_bus/school_bus.sqlite

CREATE DATABASE IF NOT EXISTS school_bus;

CREATE TABLE `school_bus`.`driver` (
    `Driver_ID` Int32,
    `Name` Nullable(String),
    `Party` Nullable(String),
    `Home_city` Nullable(String),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Driver_ID`;

CREATE TABLE `school_bus`.`school` (
    `School_ID` Int32,
    `Grade` Nullable(String),
    `School` Nullable(String),
    `Location` Nullable(String),
    `Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `School_ID`;

CREATE TABLE `school_bus`.`school_bus` (
    `School_ID` Int32,
    `Driver_ID` Int32,
    `Years_Working` Nullable(Int32),
    `If_full_time` Nullable(UInt8)
)
ENGINE = MergeTree()
ORDER BY (`School_ID`, `Driver_ID`);

