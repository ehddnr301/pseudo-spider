-- ClickHouse DDL for database: gymnast
-- Generated from: spider_data/database/gymnast/gymnast.sqlite

CREATE DATABASE IF NOT EXISTS gymnast;

CREATE TABLE `gymnast`.`gymnast` (
    `Gymnast_ID` Int32,
    `Floor_Exercise_Points` Nullable(Float64),
    `Pommel_Horse_Points` Nullable(Float64),
    `Rings_Points` Nullable(Float64),
    `Vault_Points` Nullable(Float64),
    `Parallel_Bars_Points` Nullable(Float64),
    `Horizontal_Bar_Points` Nullable(Float64),
    `Total_Points` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Gymnast_ID`;

CREATE TABLE `gymnast`.`people` (
    `People_ID` Int32,
    `Name` Nullable(String),
    `Age` Nullable(Float64),
    `Height` Nullable(Float64),
    `Hometown` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

