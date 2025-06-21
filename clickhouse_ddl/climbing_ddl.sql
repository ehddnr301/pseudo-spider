-- ClickHouse DDL for database: climbing
-- Generated from: spider_data/database/climbing/climbing.sqlite

CREATE DATABASE IF NOT EXISTS climbing;

CREATE TABLE `climbing`.`mountain` (
    `Mountain_ID` Int32,
    `Name` Nullable(String),
    `Height` Nullable(Float64),
    `Prominence` Nullable(Float64),
    `Range` Nullable(String),
    `Country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Mountain_ID`;

CREATE TABLE `climbing`.`climber` (
    `Climber_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `Time` Nullable(String),
    `Points` Nullable(Float64),
    `Mountain_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Climber_ID`;

