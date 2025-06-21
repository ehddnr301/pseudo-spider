-- ClickHouse DDL for database: geo
-- Generated from: spider_data/database/geo/geo.sqlite

CREATE DATABASE IF NOT EXISTS geo;

CREATE TABLE `geo`.`state` (
    `state_name` String,
    `population` Nullable(Int64),
    `area` Nullable(Float64),
    `country_name` String DEFAULT '',
    `capital` Nullable(String),
    `density` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `state_name`;

CREATE TABLE `geo`.`city` (
    `city_name` String,
    `population` Nullable(Int64),
    `country_name` String DEFAULT '',
    `state_name` String
)
ENGINE = MergeTree()
ORDER BY (`city_name`, `state_name`);

CREATE TABLE `geo`.`border_info` (
    `state_name` String,
    `border` String
)
ENGINE = MergeTree()
ORDER BY (`state_name`, `border`);

CREATE TABLE `geo`.`highlow` (
    `state_name` String,
    `highest_elevation` Nullable(String),
    `lowest_point` Nullable(String),
    `highest_point` Nullable(String),
    `lowest_elevation` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `state_name`;

CREATE TABLE `geo`.`lake` (
    `lake_name` Nullable(String),
    `area` Nullable(Float64),
    `country_name` String DEFAULT '',
    `state_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `country_name`;

CREATE TABLE `geo`.`mountain` (
    `mountain_name` String,
    `mountain_altitude` Nullable(Int64),
    `country_name` String DEFAULT '',
    `state_name` String
)
ENGINE = MergeTree()
ORDER BY (`mountain_name`, `state_name`);

CREATE TABLE `geo`.`river` (
    `river_name` String,
    `length` Nullable(Int64),
    `country_name` String DEFAULT '',
    `traverse` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `river_name`;

