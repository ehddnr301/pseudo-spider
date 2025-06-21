-- ClickHouse DDL for database: storm_record
-- Generated from: spider_data/database/storm_record/storm_record.sqlite

CREATE DATABASE IF NOT EXISTS storm_record;

CREATE TABLE `storm_record`.`storm` (
    `Storm_ID` Int32,
    `Name` Nullable(String),
    `Dates_active` Nullable(String),
    `Max_speed` Nullable(Int32),
    `Damage_millions_USD` Nullable(Float64),
    `Number_Deaths` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Storm_ID`;

CREATE TABLE `storm_record`.`region` (
    `Region_id` Int32,
    `Region_code` Nullable(String),
    `Region_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Region_id`;

CREATE TABLE `storm_record`.`affected_region` (
    `Region_id` Int32,
    `Storm_ID` Int32,
    `Number_city_affected` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Region_id`, `Storm_ID`);

