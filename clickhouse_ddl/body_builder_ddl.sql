-- ClickHouse DDL for database: body_builder
-- Generated from: spider_data/database/body_builder/body_builder.sqlite

CREATE DATABASE IF NOT EXISTS body_builder;

CREATE TABLE `body_builder`.`body_builder` (
    `Body_Builder_ID` Int32,
    `People_ID` Nullable(Int32),
    `Snatch` Nullable(Float64),
    `Clean_Jerk` Nullable(Float64),
    `Total` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Body_Builder_ID`;

CREATE TABLE `body_builder`.`people` (
    `People_ID` Int32,
    `Name` Nullable(String),
    `Height` Nullable(Float64),
    `Weight` Nullable(Float64),
    `Birth_Date` Nullable(String),
    `Birth_Place` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

