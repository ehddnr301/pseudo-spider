-- ClickHouse DDL for database: customer_complaints
-- Generated from: spider_data/database/customer_complaints/customer_complaints.sqlite

CREATE DATABASE IF NOT EXISTS customer_complaints;

CREATE TABLE `customer_complaints`.`Staff` (
    `staff_id` Int64,
    `gender` Nullable(String),
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `email_address` Nullable(String),
    `phone_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `customer_complaints`.`Customers` (
    `customer_id` Int64,
    `customer_type_code` String,
    `address_line_1` Nullable(String),
    `address_line_2` Nullable(String),
    `town_city` Nullable(String),
    `state` Nullable(String),
    `email_address` Nullable(String),
    `phone_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customer_complaints`.`Products` (
    `product_id` Int64,
    `parent_product_id` Nullable(Int64),
    `product_category_code` String,
    `date_product_first_available` Nullable(DateTime),
    `date_product_discontinued` Nullable(DateTime),
    `product_name` Nullable(String),
    `product_description` Nullable(String),
    `product_price` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customer_complaints`.`Complaints` (
    `complaint_id` Int64,
    `product_id` Int64,
    `customer_id` Int64,
    `complaint_outcome_code` String,
    `complaint_status_code` String,
    `complaint_type_code` String,
    `date_complaint_raised` Nullable(DateTime),
    `date_complaint_closed` Nullable(DateTime),
    `staff_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `staff_id`);

