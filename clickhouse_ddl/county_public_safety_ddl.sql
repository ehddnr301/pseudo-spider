-- ClickHouse DDL for database: county_public_safety
-- Generated from: spider_data/database/county_public_safety/county_public_safety.sqlite

CREATE DATABASE IF NOT EXISTS county_public_safety;

CREATE TABLE `county_public_safety`.`county_public_safety` (
    `County_ID` Int32,
    `Name` Nullable(String),
    `Population` Nullable(Int32),
    `Police_officers` Nullable(Int32),
    `Residents_per_officer` Nullable(Int32),
    `Case_burden` Nullable(Int32),
    `Crime_rate` Nullable(Float64),
    `Police_force` Nullable(String),
    `Location` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `County_ID`;

CREATE TABLE `county_public_safety`.`city` (
    `City_ID` Int32,
    `County_ID` Nullable(Int32),
    `Name` Nullable(String),
    `White` Nullable(Float64),
    `Black` Nullable(Float64),
    `Amerindian` Nullable(Float64),
    `Asian` Nullable(Float64),
    `Multiracial` Nullable(Float64),
    `Hispanic` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `City_ID`;

