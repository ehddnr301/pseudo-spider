-- ClickHouse DDL for database: ship_mission
-- Generated from: spider_data/database/ship_mission/ship_mission.sqlite

CREATE DATABASE IF NOT EXISTS ship_mission;

CREATE TABLE `ship_mission`.`mission` (
    `Mission_ID` Int32,
    `Ship_ID` Nullable(Int32),
    `Code` Nullable(String),
    `Launched_Year` Nullable(Int32),
    `Location` Nullable(String),
    `Speed_knots` Nullable(Int32),
    `Fate` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Mission_ID`;

CREATE TABLE `ship_mission`.`ship` (
    `Ship_ID` Int32,
    `Name` Nullable(String),
    `Type` Nullable(String),
    `Nationality` Nullable(String),
    `Tonnage` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Ship_ID`;

