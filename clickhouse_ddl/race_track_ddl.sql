-- ClickHouse DDL for database: race_track
-- Generated from: spider_data/database/race_track/race_track.sqlite

CREATE DATABASE IF NOT EXISTS race_track;

CREATE TABLE `race_track`.`race` (
    `Race_ID` Int32,
    `Name` Nullable(String),
    `Class` Nullable(String),
    `Date` Nullable(String),
    `Track_ID` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Race_ID`;

CREATE TABLE `race_track`.`track` (
    `Track_ID` Int32,
    `Name` Nullable(String),
    `Location` Nullable(String),
    `Seating` Nullable(Float64),
    `Year_Opened` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Track_ID`;

