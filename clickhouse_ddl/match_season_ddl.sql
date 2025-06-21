-- ClickHouse DDL for database: match_season
-- Generated from: spider_data/database/match_season/match_season.sqlite

CREATE DATABASE IF NOT EXISTS match_season;

CREATE TABLE `match_season`.`country` (
    `Country_id` Int32,
    `Country_name` Nullable(String),
    `Capital` Nullable(String),
    `Official_native_language` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Country_id`;

CREATE TABLE `match_season`.`team` (
    `Team_id` Int32,
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Team_id`;

CREATE TABLE `match_season`.`match_season` (
    `Season` Float64,
    `Player` Nullable(String),
    `Position` Nullable(String),
    `Country` Nullable(Int32),
    `Team` Nullable(Int32),
    `Draft_Pick_Number` Nullable(Int32),
    `Draft_Class` Nullable(String),
    `College` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Season`;

CREATE TABLE `match_season`.`player` (
    `Player_ID` Int32,
    `Player` Nullable(String),
    `Years_Played` Nullable(String),
    `Total_WL` Nullable(String),
    `Singles_WL` Nullable(String),
    `Doubles_WL` Nullable(String),
    `Team` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Player_ID`;

