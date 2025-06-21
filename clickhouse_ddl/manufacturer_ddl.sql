-- ClickHouse DDL for database: manufacturer
-- Generated from: spider_data/database/manufacturer/manufacturer.sqlite

CREATE DATABASE IF NOT EXISTS manufacturer;

CREATE TABLE `manufacturer`.`manufacturer` (
    `Manufacturer_ID` Int32,
    `Open_Year` Nullable(Float64),
    `Name` Nullable(String),
    `Num_of_Factories` Nullable(Int32),
    `Num_of_Shops` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Manufacturer_ID`;

CREATE TABLE `manufacturer`.`furniture` (
    `Furniture_ID` Int32,
    `Name` Nullable(String),
    `Num_of_Component` Nullable(Int32),
    `Market_Rate` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Furniture_ID`;

CREATE TABLE `manufacturer`.`furniture_manufacte` (
    `Manufacturer_ID` Int32,
    `Furniture_ID` Int32,
    `Price_in_Dollar` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Manufacturer_ID`, `Furniture_ID`);

