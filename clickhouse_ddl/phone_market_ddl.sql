-- ClickHouse DDL for database: phone_market
-- Generated from: spider_data/database/phone_market/phone_market.sqlite

CREATE DATABASE IF NOT EXISTS phone_market;

CREATE TABLE `phone_market`.`phone` (
    `Name` Nullable(String),
    `Phone_ID` Int32,
    `Memory_in_G` Nullable(Int32),
    `Carrier` Nullable(String),
    `Price` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Phone_ID`;

CREATE TABLE `phone_market`.`market` (
    `Market_ID` Int32,
    `District` Nullable(String),
    `Num_of_employees` Nullable(Int32),
    `Num_of_shops` Nullable(Float64),
    `Ranking` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Market_ID`;

CREATE TABLE `phone_market`.`phone_market` (
    `Market_ID` Int32,
    `Phone_ID` String,
    `Num_of_stock` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Market_ID`, `Phone_ID`);

