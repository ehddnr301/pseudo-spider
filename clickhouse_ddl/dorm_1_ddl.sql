-- ClickHouse DDL for database: dorm_1
-- Generated from: spider_data/database/dorm_1/dorm_1.sqlite

CREATE DATABASE IF NOT EXISTS dorm_1;

CREATE TABLE `dorm_1`.`Student` (
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

CREATE TABLE `dorm_1`.`Dorm` (
    `dormid` Nullable(Int64),
    `dorm_name` Nullable(String),
    `student_capacity` Nullable(Int64),
    `gender` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `dorm_1`.`Dorm_amenity` (
    `amenid` Nullable(Int64),
    `amenity_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `dorm_1`.`Has_amenity` (
    `dormid` Nullable(Int64),
    `amenid` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `dorm_1`.`Lives_in` (
    `stuid` Nullable(Int64),
    `dormid` Nullable(Int64),
    `room_number` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

