-- ClickHouse DDL for database: manufactory_1
-- Generated from: spider_data/database/manufactory_1/manufactory_1.sqlite

CREATE DATABASE IF NOT EXISTS manufactory_1;

CREATE TABLE `manufactory_1`.`Manufacturers` (
    `Code` Int64,
    `Name` String,
    `Headquarter` String,
    `Founder` String,
    `Revenue` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Code`;

CREATE TABLE `manufactory_1`.`Products` (
    `Code` Int64,
    `Name` String,
    `Price` Decimal64(2),
    `Manufacturer` Int64
)
ENGINE = MergeTree()
ORDER BY `Code`;

