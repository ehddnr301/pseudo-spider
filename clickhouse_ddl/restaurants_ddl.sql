-- ClickHouse DDL for database: restaurants
-- Generated from: spider_data/database/restaurants/restaurants.sqlite

CREATE DATABASE IF NOT EXISTS restaurants;

CREATE TABLE `restaurants`.`GEOGRAPHIC` (
    `CITY_NAME` String,
    `COUNTY` Nullable(String),
    `REGION` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `CITY_NAME`;

CREATE TABLE `restaurants`.`RESTAURANT` (
    `ID` Int32,
    `NAME` Nullable(String),
    `FOOD_TYPE` Nullable(String),
    `CITY_NAME` Nullable(String),
    `RATING` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `restaurants`.`LOCATION` (
    `RESTAURANT_ID` Int32,
    `HOUSE_NUMBER` Nullable(Int32),
    `STREET_NAME` Nullable(String),
    `CITY_NAME` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `RESTAURANT_ID`;

