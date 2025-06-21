-- ClickHouse DDL for database: customers_and_products_contacts
-- Generated from: spider_data/database/customers_and_products_contacts/customers_and_products_contacts.sqlite

CREATE DATABASE IF NOT EXISTS customers_and_products_contacts;

CREATE TABLE `customers_and_products_contacts`.`Addresses` (
    `address_id` Int64,
    `line_1_number_building` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `customers_and_products_contacts`.`Products` (
    `product_id` Int64,
    `product_type_code` Nullable(String),
    `product_name` Nullable(String),
    `product_price` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customers_and_products_contacts`.`Customers` (
    `customer_id` Int64,
    `payment_method_code` Nullable(String),
    `customer_number` Nullable(String),
    `customer_name` Nullable(String),
    `customer_address` Nullable(String),
    `customer_phone` Nullable(String),
    `customer_email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customers_and_products_contacts`.`Contacts` (
    `contact_id` Int64,
    `customer_id` Int64,
    `gender` Nullable(String),
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `contact_phone` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `contact_id`;

CREATE TABLE `customers_and_products_contacts`.`Customer_Address_History` (
    `customer_id` Int64,
    `address_id` Int64,
    `date_from` DateTime,
    `date_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `address_id`, `date_from`);

CREATE TABLE `customers_and_products_contacts`.`Customer_Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `order_date` DateTime,
    `order_status_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `customers_and_products_contacts`.`Order_Items` (
    `order_item_id` Int64,
    `order_id` Int64,
    `product_id` Int64,
    `order_quantity` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`order_item_id`, `order_id`, `product_id`);

