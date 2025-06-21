-- ClickHouse DDL for database: wine_1
-- Generated from: spider_data/database/wine_1/wine_1.sqlite

CREATE DATABASE IF NOT EXISTS wine_1;

CREATE TABLE `wine_1`.`grapes` (
    `ID` Int64,
    `Grape` Nullable(String),
    `Color` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `wine_1`.`appellations` (
    `No` Int64,
    `Appelation` Nullable(String),
    `County` Nullable(String),
    `State` Nullable(String),
    `Area` Nullable(String),
    `isAVA` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `No`;

CREATE TABLE `wine_1`.`wine` (
    `No` Nullable(Int64),
    `Grape` Nullable(String),
    `Winery` Nullable(String),
    `Appelation` Nullable(String),
    `State` Nullable(String),
    `Name` Nullable(String),
    `Year` Nullable(Int64),
    `Price` Nullable(Int64),
    `Score` Nullable(Int64),
    `Cases` Nullable(Int64),
    `Drink` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

