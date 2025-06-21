-- ClickHouse DDL for database: game_1
-- Generated from: spider_data/database/game_1/game_1.sqlite

CREATE DATABASE IF NOT EXISTS game_1;

CREATE TABLE `game_1`.`Student` (
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

CREATE TABLE `game_1`.`Video_Games` (
    `GameID` Int64,
    `GName` Nullable(String),
    `GType` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `GameID`;

CREATE TABLE `game_1`.`Plays_Games` (
    `StuID` Nullable(Int64),
    `GameID` Nullable(Int64),
    `Hours_Played` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `game_1`.`SportsInfo` (
    `StuID` Nullable(Int64),
    `SportName` Nullable(String),
    `HoursPerWeek` Nullable(Int64),
    `GamesPlayed` Nullable(Int64),
    `OnScholarship` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

