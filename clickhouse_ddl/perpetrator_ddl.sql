-- ClickHouse DDL for database: perpetrator
-- Generated from: spider_data/database/perpetrator/perpetrator.sqlite

CREATE DATABASE IF NOT EXISTS perpetrator;

CREATE TABLE `perpetrator`.`perpetrator` (
    `Perpetrator_ID` Int32,
    `People_ID` Nullable(Int32),
    `Date` Nullable(String),
    `Year` Nullable(Float64),
    `Location` Nullable(String),
    `Country` Nullable(String),
    `Killed` Nullable(Int32),
    `Injured` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Perpetrator_ID`;

CREATE TABLE `perpetrator`.`people` (
    `People_ID` Int32,
    `Name` Nullable(String),
    `Height` Nullable(Float64),
    `Weight` Nullable(Float64),
    `Home Town` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

