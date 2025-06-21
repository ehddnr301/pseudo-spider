-- ClickHouse DDL for database: election
-- Generated from: spider_data/database/election/election.sqlite

CREATE DATABASE IF NOT EXISTS election;

CREATE TABLE `election`.`county` (
    `County_Id` Int32,
    `County_name` Nullable(String),
    `Population` Nullable(Float64),
    `Zip_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `County_Id`;

CREATE TABLE `election`.`party` (
    `Party_ID` Int32,
    `Year` Nullable(Float64),
    `Party` Nullable(String),
    `Governor` Nullable(String),
    `Lieutenant_Governor` Nullable(String),
    `Comptroller` Nullable(String),
    `Attorney_General` Nullable(String),
    `US_Senate` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Party_ID`;

CREATE TABLE `election`.`election` (
    `Election_ID` Int32,
    `Counties_Represented` Nullable(String),
    `District` Nullable(Int32),
    `Delegate` Nullable(String),
    `Party` Nullable(Int32),
    `First_Elected` Nullable(Float64),
    `Committee` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Election_ID`;

