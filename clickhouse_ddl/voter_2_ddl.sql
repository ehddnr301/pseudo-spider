-- ClickHouse DDL for database: voter_2
-- Generated from: spider_data/database/voter_2/voter_2.sqlite

CREATE DATABASE IF NOT EXISTS voter_2;

CREATE TABLE `voter_2`.`Student` (
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

CREATE TABLE `voter_2`.`Voting_record` (
    `StuID` Nullable(Int64),
    `Registration_Date` Nullable(String),
    `Election_Cycle` Nullable(String),
    `President_Vote` Nullable(Int64),
    `Vice_President_Vote` Nullable(Int64),
    `Secretary_Vote` Nullable(Int64),
    `Treasurer_Vote` Nullable(Int64),
    `Class_President_Vote` Nullable(Int64),
    `Class_Senator_Vote` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

