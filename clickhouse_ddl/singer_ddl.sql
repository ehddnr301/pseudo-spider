-- ClickHouse DDL for database: singer
-- Generated from: spider_data/database/singer/singer.sqlite

CREATE DATABASE IF NOT EXISTS singer;

CREATE TABLE `singer`.`singer` (
    `Singer_ID` Int32,
    `Name` Nullable(String),
    `Birth_Year` Nullable(Float64),
    `Net_Worth_Millions` Nullable(Float64),
    `Citizenship` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Singer_ID`;

CREATE TABLE `singer`.`song` (
    `Song_ID` Int32,
    `Title` Nullable(String),
    `Singer_ID` Nullable(Int32),
    `Sales` Nullable(Float64),
    `Highest_Position` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Song_ID`;

