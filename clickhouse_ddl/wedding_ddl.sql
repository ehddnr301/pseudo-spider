-- ClickHouse DDL for database: wedding
-- Generated from: spider_data/database/wedding/wedding.sqlite

CREATE DATABASE IF NOT EXISTS wedding;

CREATE TABLE `wedding`.`people` (
    `People_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `Is_Male` Nullable(String),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

CREATE TABLE `wedding`.`church` (
    `Church_ID` Int32,
    `Name` Nullable(String),
    `Organized_by` Nullable(String),
    `Open_Date` Nullable(Int32),
    `Continuation_of` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Church_ID`;

CREATE TABLE `wedding`.`wedding` (
    `Church_ID` Int32,
    `Male_ID` Int32,
    `Female_ID` Int32,
    `Year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Church_ID`, `Male_ID`, `Female_ID`);

