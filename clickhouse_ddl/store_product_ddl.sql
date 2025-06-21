-- ClickHouse DDL for database: store_product
-- Generated from: spider_data/database/store_product/store_product.sqlite

CREATE DATABASE IF NOT EXISTS store_product;

CREATE TABLE `store_product`.`product` (
    `product_id` Int32,
    `product` Nullable(String),
    `dimensions` Nullable(String),
    `dpi` Nullable(Float64),
    `pages_per_minute_color` Nullable(Float64),
    `max_page_size` Nullable(String),
    `interface` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `store_product`.`store` (
    `Store_ID` Int32,
    `Store_Name` Nullable(String),
    `Type` Nullable(String),
    `Area_size` Nullable(Float64),
    `Number_of_product_category` Nullable(Float64),
    `Ranking` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Store_ID`;

CREATE TABLE `store_product`.`district` (
    `District_ID` Int32,
    `District_name` Nullable(String),
    `Headquartered_City` Nullable(String),
    `City_Population` Nullable(Float64),
    `City_Area` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `District_ID`;

CREATE TABLE `store_product`.`store_product` (
    `Store_ID` Int32,
    `Product_ID` Int32
)
ENGINE = MergeTree()
ORDER BY (`Store_ID`, `Product_ID`);

CREATE TABLE `store_product`.`store_district` (
    `Store_ID` Int32,
    `District_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Store_ID`;

