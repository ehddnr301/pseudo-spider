-- ClickHouse DDL for database: entrepreneur
-- Generated from: spider_data/database/entrepreneur/entrepreneur.sqlite

CREATE DATABASE IF NOT EXISTS entrepreneur;

CREATE TABLE `entrepreneur`.`entrepreneur` (
    `Entrepreneur_ID` Int32,
    `People_ID` Nullable(Int32),
    `Company` Nullable(String),
    `Money_Requested` Nullable(Float64),
    `Investor` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Entrepreneur_ID`;

CREATE TABLE `entrepreneur`.`people` (
    `People_ID` Int32,
    `Name` Nullable(String),
    `Height` Nullable(Float64),
    `Weight` Nullable(Float64),
    `Date_of_Birth` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

