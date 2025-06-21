-- ClickHouse DDL for database: soccer_2
-- Generated from: spider_data/database/soccer_2/soccer_2.sqlite

CREATE DATABASE IF NOT EXISTS soccer_2;

CREATE TABLE `soccer_2`.`College` (
    `cName` String,
    `state` Nullable(String),
    `enr` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `cName`;

CREATE TABLE `soccer_2`.`Player` (
    `pID` Decimal64(2),
    `pName` Nullable(String),
    `yCard` Nullable(String),
    `HS` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `pID`;

CREATE TABLE `soccer_2`.`Tryout` (
    `pID` Decimal64(2),
    `cName` String,
    `pPos` Nullable(String),
    `decision` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`pID`, `cName`);

