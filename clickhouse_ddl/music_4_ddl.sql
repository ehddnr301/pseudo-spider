-- ClickHouse DDL for database: music_4
-- Generated from: spider_data/database/music_4/music_4.sqlite

CREATE DATABASE IF NOT EXISTS music_4;

CREATE TABLE `music_4`.`artist` (
    `Artist_ID` Int32,
    `Artist` Nullable(String),
    `Age` Nullable(Int32),
    `Famous_Title` Nullable(String),
    `Famous_Release_date` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Artist_ID`;

CREATE TABLE `music_4`.`volume` (
    `Volume_ID` Int32,
    `Volume_Issue` Nullable(String),
    `Issue_Date` Nullable(String),
    `Weeks_on_Top` Nullable(Float64),
    `Song` Nullable(String),
    `Artist_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Volume_ID`;

CREATE TABLE `music_4`.`music_festival` (
    `ID` Int32,
    `Music_Festival` Nullable(String),
    `Date_of_ceremony` Nullable(String),
    `Category` Nullable(String),
    `Volume` Nullable(Int32),
    `Result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ID`;

