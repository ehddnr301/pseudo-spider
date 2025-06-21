-- ClickHouse DDL for database: program_share
-- Generated from: spider_data/database/program_share/program_share.sqlite

CREATE DATABASE IF NOT EXISTS program_share;

CREATE TABLE `program_share`.`program` (
    `Program_ID` Int32,
    `Name` Nullable(String),
    `Origin` Nullable(String),
    `Launch` Nullable(Float64),
    `Owner` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Program_ID`;

CREATE TABLE `program_share`.`channel` (
    `Channel_ID` Int32,
    `Name` Nullable(String),
    `Owner` Nullable(String),
    `Share_in_percent` Nullable(Float64),
    `Rating_in_percent` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Channel_ID`;

CREATE TABLE `program_share`.`broadcast` (
    `Channel_ID` Int32,
    `Program_ID` Int32,
    `Time_of_day` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Channel_ID`, `Program_ID`);

CREATE TABLE `program_share`.`broadcast_share` (
    `Channel_ID` Int32,
    `Program_ID` Int32,
    `Date` Nullable(String),
    `Share_in_percent` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Channel_ID`, `Program_ID`);

