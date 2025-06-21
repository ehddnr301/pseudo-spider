-- ClickHouse DDL for database: club_1
-- Generated from: spider_data/database/club_1/club_1.sqlite

CREATE DATABASE IF NOT EXISTS club_1;

CREATE TABLE `club_1`.`Student` (
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

CREATE TABLE `club_1`.`Club` (
    `ClubID` Int64,
    `ClubName` Nullable(String),
    `ClubDesc` Nullable(String),
    `ClubLocation` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ClubID`;

CREATE TABLE `club_1`.`Member_of_club` (
    `StuID` Nullable(Int64),
    `ClubID` Nullable(Int64),
    `Position` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

