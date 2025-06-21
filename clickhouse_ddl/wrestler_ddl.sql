-- ClickHouse DDL for database: wrestler
-- Generated from: spider_data/database/wrestler/wrestler.sqlite

CREATE DATABASE IF NOT EXISTS wrestler;

CREATE TABLE `wrestler`.`wrestler` (
    `Wrestler_ID` Int32,
    `Name` Nullable(String),
    `Reign` Nullable(String),
    `Days_held` Nullable(String),
    `Location` Nullable(String),
    `Event` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Wrestler_ID`;

CREATE TABLE `wrestler`.`Elimination` (
    `Elimination_ID` String,
    `Wrestler_ID` Nullable(String),
    `Team` Nullable(String),
    `Eliminated_By` Nullable(String),
    `Elimination_Move` Nullable(String),
    `Time` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Elimination_ID`;

