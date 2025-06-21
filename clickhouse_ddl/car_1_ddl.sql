-- ClickHouse DDL for database: car_1
-- Generated from: spider_data/database/car_1/car_1.sqlite

CREATE DATABASE IF NOT EXISTS car_1;

CREATE TABLE `car_1`.`continents` (
    `ContId` Int64,
    `Continent` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ContId`;

CREATE TABLE `car_1`.`countries` (
    `CountryId` Int64,
    `CountryName` Nullable(String),
    `Continent` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `CountryId`;

CREATE TABLE `car_1`.`car_makers` (
    `Id` Int64,
    `Maker` Nullable(String),
    `FullName` Nullable(String),
    `Country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Id`;

CREATE TABLE `car_1`.`model_list` (
    `ModelId` Int64,
    `Maker` Nullable(Int64),
    `Model` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ModelId`;

CREATE TABLE `car_1`.`car_names` (
    `MakeId` Int64,
    `Model` Nullable(String),
    `Make` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `MakeId`;

CREATE TABLE `car_1`.`cars_data` (
    `Id` Int64,
    `MPG` Nullable(String),
    `Cylinders` Nullable(Int64),
    `Edispl` Nullable(Float64),
    `Horsepower` Nullable(String),
    `Weight` Nullable(Int64),
    `Accelerate` Nullable(Float64),
    `Year` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Id`;

