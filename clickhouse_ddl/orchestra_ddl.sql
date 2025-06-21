-- ClickHouse DDL for database: orchestra
-- Generated from: spider_data/database/orchestra/orchestra.sqlite

CREATE DATABASE IF NOT EXISTS orchestra;

CREATE TABLE `orchestra`.`conductor` (
    `Conductor_ID` Int32,
    `Name` Nullable(String),
    `Age` Nullable(Int32),
    `Nationality` Nullable(String),
    `Year_of_Work` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Conductor_ID`;

CREATE TABLE `orchestra`.`orchestra` (
    `Orchestra_ID` Int32,
    `Orchestra` Nullable(String),
    `Conductor_ID` Nullable(Int32),
    `Record_Company` Nullable(String),
    `Year_of_Founded` Nullable(Float64),
    `Major_Record_Format` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Orchestra_ID`;

CREATE TABLE `orchestra`.`performance` (
    `Performance_ID` Int32,
    `Orchestra_ID` Nullable(Int32),
    `Type` Nullable(String),
    `Date` Nullable(String),
    `Official_ratings_(millions)` Nullable(Float64),
    `Weekly_rank` Nullable(String),
    `Share` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Performance_ID`;

CREATE TABLE `orchestra`.`show` (
    `Show_ID` Nullable(Int32),
    `Performance_ID` Nullable(Int32),
    `If_first_show` Nullable(UInt8),
    `Result` Nullable(String),
    `Attendance` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY tuple();

