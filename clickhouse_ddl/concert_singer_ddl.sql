-- ClickHouse DDL for database: concert_singer
-- Generated from: spider_data/database/concert_singer/concert_singer.sqlite

CREATE DATABASE IF NOT EXISTS concert_singer;

CREATE TABLE `concert_singer`.`stadium` (
    `Stadium_ID` Int32,
    `Location` Nullable(String),
    `Name` Nullable(String),
    `Capacity` Nullable(Int32),
    `Highest` Nullable(Int32),
    `Lowest` Nullable(Int32),
    `Average` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Stadium_ID`;

CREATE TABLE `concert_singer`.`singer` (
    `Singer_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `Song_Name` Nullable(String),
    `Song_release_year` Nullable(String),
    `Age` Nullable(Int32),
    `Is_male` Nullable(UInt8)
)
ENGINE = MergeTree()
ORDER BY `Singer_ID`;

CREATE TABLE `concert_singer`.`concert` (
    `concert_ID` Int32,
    `concert_Name` Nullable(String),
    `Theme` Nullable(String),
    `Stadium_ID` Nullable(String),
    `Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `concert_ID`;

CREATE TABLE `concert_singer`.`singer_in_concert` (
    `concert_ID` Int32,
    `Singer_ID` String
)
ENGINE = MergeTree()
ORDER BY (`concert_ID`, `Singer_ID`);

