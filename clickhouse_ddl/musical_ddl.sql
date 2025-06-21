-- ClickHouse DDL for database: musical
-- Generated from: spider_data/database/musical/musical.sqlite

CREATE DATABASE IF NOT EXISTS musical;

CREATE TABLE `musical`.`musical` (
    `Musical_ID` Int32,
    `Name` Nullable(String),
    `Year` Nullable(Int32),
    `Award` Nullable(String),
    `Category` Nullable(String),
    `Nominee` Nullable(String),
    `Result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Musical_ID`;

CREATE TABLE `musical`.`actor` (
    `Actor_ID` Int32,
    `Name` Nullable(String),
    `Musical_ID` Nullable(Int32),
    `Character` Nullable(String),
    `Duration` Nullable(String),
    `age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Actor_ID`;

