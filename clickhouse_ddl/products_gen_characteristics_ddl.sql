-- ClickHouse DDL for database: products_gen_characteristics
-- Generated from: spider_data/database/products_gen_characteristics/products_gen_characteristics.sqlite

CREATE DATABASE IF NOT EXISTS products_gen_characteristics;

CREATE TABLE `products_gen_characteristics`.`Ref_Characteristic_Types` (
    `characteristic_type_code` String,
    `characteristic_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `characteristic_type_code`;

CREATE TABLE `products_gen_characteristics`.`Ref_Colors` (
    `color_code` String,
    `color_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `color_code`;

CREATE TABLE `products_gen_characteristics`.`Ref_Product_Categories` (
    `product_category_code` String,
    `product_category_description` Nullable(String),
    `unit_of_measure` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_category_code`;

CREATE TABLE `products_gen_characteristics`.`Characteristics` (
    `characteristic_id` Int64,
    `characteristic_type_code` String,
    `characteristic_data_type` Nullable(String),
    `characteristic_name` Nullable(String),
    `other_characteristic_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `characteristic_id`;

CREATE TABLE `products_gen_characteristics`.`Products` (
    `product_id` Int64,
    `color_code` String,
    `product_category_code` String,
    `product_name` Nullable(String),
    `typical_buying_price` Nullable(String),
    `typical_selling_price` Nullable(String),
    `product_description` Nullable(String),
    `other_product_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `products_gen_characteristics`.`Product_Characteristics` (
    `product_id` Int64,
    `characteristic_id` Int64,
    `product_characteristic_value` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`product_id`, `characteristic_id`);

