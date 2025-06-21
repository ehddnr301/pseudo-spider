-- ClickHouse DDL for database: sports_competition
-- Generated from: spider_data/database/sports_competition/sports_competition.sqlite

CREATE DATABASE IF NOT EXISTS sports_competition;

CREATE TABLE `sports_competition`.`club` (
    `Club_ID` Int32,
    `name` Nullable(String),
    `Region` Nullable(String),
    `Start_year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Club_ID`;

CREATE TABLE `sports_competition`.`club_rank` (
    `Rank` Float64,
    `Club_ID` Int32,
    `Gold` Nullable(Float64),
    `Silver` Nullable(Float64),
    `Bronze` Nullable(Float64),
    `Total` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Rank`, `Club_ID`);

CREATE TABLE `sports_competition`.`player` (
    `Player_ID` Int32,
    `name` Nullable(String),
    `Position` Nullable(String),
    `Club_ID` Nullable(Int32),
    `Apps` Nullable(Float64),
    `Tries` Nullable(Float64),
    `Goals` Nullable(String),
    `Points` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Player_ID`;

CREATE TABLE `sports_competition`.`competition` (
    `Competition_ID` Int32,
    `Year` Nullable(Float64),
    `Competition_type` Nullable(String),
    `Country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Competition_ID`;

CREATE TABLE `sports_competition`.`competition_result` (
    `Competition_ID` Int32,
    `Club_ID_1` Int32,
    `Club_ID_2` Int32,
    `Score` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Competition_ID`, `Club_ID_1`, `Club_ID_2`);

