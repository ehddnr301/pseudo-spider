-- ClickHouse DDL for database: activity_1
-- Generated from: spider_data/database/activity_1/activity_1.sqlite

CREATE DATABASE IF NOT EXISTS activity_1;

CREATE TABLE `activity_1`.`Activity` (
    `actid` Int64,
    `activity_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `actid`;

CREATE TABLE `activity_1`.`Participates_in` (
    `stuid` Nullable(Int64),
    `actid` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `activity_1`.`Faculty_Participates_in` (
    `FacID` Nullable(Int64),
    `actid` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `activity_1`.`Student` (
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

CREATE TABLE `activity_1`.`Faculty` (
    `FacID` Int64,
    `Lname` Nullable(String),
    `Fname` Nullable(String),
    `Rank` Nullable(String),
    `Sex` Nullable(String),
    `Phone` Nullable(Int64),
    `Room` Nullable(String),
    `Building` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `FacID`;

