-- ClickHouse DDL for database: riding_club
-- Generated from: spider_data/database/riding_club/riding_club.sqlite

CREATE DATABASE IF NOT EXISTS riding_club;

CREATE TABLE `riding_club`.`player` (
    `Player_ID` Int32,
    `Sponsor_name` Nullable(String),
    `Player_name` Nullable(String),
    `Gender` Nullable(String),
    `Residence` Nullable(String),
    `Occupation` Nullable(String),
    `Votes` Nullable(Int32),
    `Rank` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Player_ID`;

CREATE TABLE `riding_club`.`club` (
    `Club_ID` Int32,
    `Club_name` Nullable(String),
    `Region` Nullable(String),
    `Start_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Club_ID`;

CREATE TABLE `riding_club`.`coach` (
    `Coach_ID` Int32,
    `Coach_name` Nullable(String),
    `Gender` Nullable(String),
    `Club_ID` Nullable(Int32),
    `Rank` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Coach_ID`;

CREATE TABLE `riding_club`.`player_coach` (
    `Player_ID` Int32,
    `Coach_ID` Int32,
    `Starting_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Player_ID`, `Coach_ID`);

CREATE TABLE `riding_club`.`match_result` (
    `Rank` Int32,
    `Club_ID` Int32,
    `Gold` Nullable(Int32),
    `Big_Silver` Nullable(Int32),
    `Small_Silver` Nullable(Int32),
    `Bronze` Nullable(Int32),
    `Points` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Rank`, `Club_ID`);

