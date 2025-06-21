-- ClickHouse DDL for database: decoration_competition
-- Generated from: spider_data/database/decoration_competition/decoration_competition.sqlite

CREATE DATABASE IF NOT EXISTS decoration_competition;

CREATE TABLE `decoration_competition`.`college` (
    `College_ID` Int32,
    `Name` Nullable(String),
    `Leader_Name` Nullable(String),
    `College_Location` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `College_ID`;

CREATE TABLE `decoration_competition`.`member` (
    `Member_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `College_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `decoration_competition`.`round` (
    `Round_ID` Int32,
    `Member_ID` Int32,
    `Decoration_Theme` Nullable(String),
    `Rank_in_Round` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Round_ID`, `Member_ID`);

