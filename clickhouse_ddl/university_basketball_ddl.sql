-- ClickHouse DDL for database: university_basketball
-- Generated from: spider_data/database/university_basketball/university_basketball.sqlite

CREATE DATABASE IF NOT EXISTS university_basketball;

CREATE TABLE `university_basketball`.`basketball_match` (
    `Team_ID` Int32,
    `School_ID` Nullable(Int32),
    `Team_Name` Nullable(String),
    `ACC_Regular_Season` Nullable(String),
    `ACC_Percent` Nullable(String),
    `ACC_Home` Nullable(String),
    `ACC_Road` Nullable(String),
    `All_Games` Nullable(String),
    `All_Games_Percent` Nullable(Int32),
    `All_Home` Nullable(String),
    `All_Road` Nullable(String),
    `All_Neutral` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Team_ID`;

CREATE TABLE `university_basketball`.`university` (
    `School_ID` Int32,
    `School` Nullable(String),
    `Location` Nullable(String),
    `Founded` Nullable(Float64),
    `Affiliation` Nullable(String),
    `Enrollment` Nullable(Float64),
    `Nickname` Nullable(String),
    `Primary_conference` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `School_ID`;

