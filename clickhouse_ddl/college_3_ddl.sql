-- ClickHouse DDL for database: college_3
-- Generated from: spider_data/database/college_3/college_3.sqlite

CREATE DATABASE IF NOT EXISTS college_3;

CREATE TABLE `college_3`.`Student` (
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

CREATE TABLE `college_3`.`Faculty` (
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

CREATE TABLE `college_3`.`Department` (
    `DNO` Int64,
    `Division` Nullable(String),
    `DName` Nullable(String),
    `Room` Nullable(String),
    `Building` Nullable(String),
    `DPhone` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `DNO`;

CREATE TABLE `college_3`.`Member_of` (
    `FacID` Nullable(Int64),
    `DNO` Nullable(Int64),
    `Appt_Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `college_3`.`Course` (
    `CID` String,
    `CName` Nullable(String),
    `Credits` Nullable(Int64),
    `Instructor` Nullable(Int64),
    `Days` Nullable(String),
    `Hours` Nullable(String),
    `DNO` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `CID`;

CREATE TABLE `college_3`.`Minor_in` (
    `StuID` Nullable(Int64),
    `DNO` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `college_3`.`Enrolled_in` (
    `StuID` Nullable(Int64),
    `CID` Nullable(String),
    `Grade` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `college_3`.`Gradeconversion` (
    `lettergrade` String,
    `gradepoint` Nullable(Float32)
)
ENGINE = MergeTree()
ORDER BY `lettergrade`;

