-- ClickHouse DDL for database: customers_and_addresses
-- Generated from: spider_data/database/customers_and_addresses/customers_and_addresses.sqlite

CREATE DATABASE IF NOT EXISTS customers_and_addresses;

CREATE TABLE `customers_and_addresses`.`Addresses` (
    `address_id` Int64,
    `address_content` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String),
    `other_address_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `customers_and_addresses`.`Products` (
    `product_id` Int64,
    `product_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customers_and_addresses`.`Customers` (
    `customer_id` Int64,
    `payment_method` String,
    `customer_name` Nullable(String),
    `date_became_customer` Nullable(DateTime),
    `other_customer_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customers_and_addresses`.`Customer_Addresses` (
    `customer_id` Int64,
    `address_id` Int64,
    `date_address_from` DateTime,
    `address_type` String,
    `date_address_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `address_id`, `date_address_from`, `address_type`);

CREATE TABLE `customers_and_addresses`.`Customer_Contact_Channels` (
    `customer_id` Int64,
    `channel_code` String,
    `active_from_date` DateTime,
    `active_to_date` Nullable(DateTime),
    `contact_number` String
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `channel_code`, `active_from_date`, `contact_number`);

CREATE TABLE `customers_and_addresses`.`Customer_Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `order_status` String,
    `order_date` Nullable(DateTime),
    `order_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `customers_and_addresses`.`Order_Items` (
    `order_id` Int64,
    `product_id` Int64,
    `order_quantity` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`order_id`, `product_id`);

