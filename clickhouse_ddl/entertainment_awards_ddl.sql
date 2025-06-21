-- ClickHouse DDL for database: entertainment_awards
-- Generated from: spider_data/database/entertainment_awards/entertainment_awards.sqlite

CREATE DATABASE IF NOT EXISTS entertainment_awards;

CREATE TABLE `entertainment_awards`.`festival_detail` (
    `Festival_ID` Int32,
    `Festival_Name` Nullable(String),
    `Chair_Name` Nullable(String),
    `Location` Nullable(String),
    `Year` Nullable(Int32),
    `Num_of_Audience` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Festival_ID`;

CREATE TABLE `entertainment_awards`.`artwork` (
    `Artwork_ID` Int32,
    `Type` Nullable(String),
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Artwork_ID`;

CREATE TABLE `entertainment_awards`.`nomination` (
    `Artwork_ID` Int32,
    `Festival_ID` Int32,
    `Result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Artwork_ID`, `Festival_ID`);

