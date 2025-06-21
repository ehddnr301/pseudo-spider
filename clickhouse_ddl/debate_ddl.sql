-- ClickHouse DDL for database: debate
-- Generated from: spider_data/database/debate/debate.sqlite

CREATE DATABASE IF NOT EXISTS debate;

CREATE TABLE `debate`.`people` (
    `People_ID` Int32,
    `District` Nullable(String),
    `Name` Nullable(String),
    `Party` Nullable(String),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

CREATE TABLE `debate`.`debate` (
    `Debate_ID` Int32,
    `Date` Nullable(String),
    `Venue` Nullable(String),
    `Num_of_Audience` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Debate_ID`;

CREATE TABLE `debate`.`debate_people` (
    `Debate_ID` Int32,
    `Affirmative` Int32,
    `Negative` Int32,
    `If_Affirmative_Win` Nullable(UInt8)
)
ENGINE = MergeTree()
ORDER BY (`Debate_ID`, `Affirmative`, `Negative`);

