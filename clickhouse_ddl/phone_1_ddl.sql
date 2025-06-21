-- ClickHouse DDL for database: phone_1
-- Generated from: spider_data/database/phone_1/phone_1.sqlite

CREATE DATABASE IF NOT EXISTS phone_1;

CREATE TABLE `phone_1`.`chip_model` (
    `Model_name` String,
    `Launch_year` Nullable(Float64),
    `RAM_MiB` Nullable(Float64),
    `ROM_MiB` Nullable(Float64),
    `Slots` Nullable(String),
    `WiFi` Nullable(String),
    `Bluetooth` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Model_name`;

CREATE TABLE `phone_1`.`screen_mode` (
    `Graphics_mode` Float64,
    `Char_cells` Nullable(String),
    `Pixels` Nullable(String),
    `Hardware_colours` Nullable(Float64),
    `used_kb` Nullable(Float64),
    `map` Nullable(String),
    `Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Graphics_mode`;

CREATE TABLE `phone_1`.`phone` (
    `Company_name` Nullable(String),
    `Hardware_Model_name` String,
    `Accreditation_type` Nullable(String),
    `Accreditation_level` Nullable(String),
    `Date` Nullable(String),
    `chip_model` Nullable(String),
    `screen_mode` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Hardware_Model_name`;

