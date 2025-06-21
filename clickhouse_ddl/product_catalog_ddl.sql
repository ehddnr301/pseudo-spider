-- ClickHouse DDL for database: product_catalog
-- Generated from: spider_data/database/product_catalog/product_catalog.sqlite

CREATE DATABASE IF NOT EXISTS product_catalog;

CREATE TABLE `product_catalog`.`Attribute_Definitions` (
    `attribute_id` Int64,
    `attribute_name` Nullable(String),
    `attribute_data_type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `attribute_id`;

CREATE TABLE `product_catalog`.`Catalogs` (
    `catalog_id` Int64,
    `catalog_name` Nullable(String),
    `catalog_publisher` Nullable(String),
    `date_of_publication` Nullable(DateTime),
    `date_of_latest_revision` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `catalog_id`;

CREATE TABLE `product_catalog`.`Catalog_Structure` (
    `catalog_level_number` Int64,
    `catalog_id` Int64,
    `catalog_level_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `catalog_level_number`;

CREATE TABLE `product_catalog`.`Catalog_Contents` (
    `catalog_entry_id` Int64,
    `catalog_level_number` Int64,
    `parent_entry_id` Nullable(Int64),
    `previous_entry_id` Nullable(Int64),
    `next_entry_id` Nullable(Int64),
    `catalog_entry_name` Nullable(String),
    `product_stock_number` Nullable(String),
    `price_in_dollars` Nullable(Float64),
    `price_in_euros` Nullable(Float64),
    `price_in_pounds` Nullable(Float64),
    `capacity` Nullable(String),
    `length` Nullable(String),
    `height` Nullable(String),
    `width` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `catalog_entry_id`;

CREATE TABLE `product_catalog`.`Catalog_Contents_Additional_Attributes` (
    `catalog_entry_id` Int64,
    `catalog_level_number` Int64,
    `attribute_id` Int64,
    `attribute_value` String
)
ENGINE = MergeTree()
ORDER BY (`catalog_entry_id`, `catalog_level_number`, `attribute_id`, `attribute_value`);

