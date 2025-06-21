-- ClickHouse DDL for database: customers_campaigns_ecommerce
-- Generated from: spider_data/database/customers_campaigns_ecommerce/customers_campaigns_ecommerce.sqlite

CREATE DATABASE IF NOT EXISTS customers_campaigns_ecommerce;

CREATE TABLE `customers_campaigns_ecommerce`.`Premises` (
    `premise_id` Int64,
    `premises_type` String,
    `premise_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `premise_id`;

CREATE TABLE `customers_campaigns_ecommerce`.`Products` (
    `product_id` Int64,
    `product_category` String,
    `product_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customers_campaigns_ecommerce`.`Customers` (
    `customer_id` Int64,
    `payment_method` String,
    `customer_name` Nullable(String),
    `customer_phone` Nullable(String),
    `customer_email` Nullable(String),
    `customer_address` Nullable(String),
    `customer_login` Nullable(String),
    `customer_password` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customers_campaigns_ecommerce`.`Mailshot_Campaigns` (
    `mailshot_id` Int64,
    `product_category` Nullable(String),
    `mailshot_name` Nullable(String),
    `mailshot_start_date` Nullable(DateTime),
    `mailshot_end_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `mailshot_id`;

CREATE TABLE `customers_campaigns_ecommerce`.`Customer_Addresses` (
    `customer_id` Int64,
    `premise_id` Int64,
    `date_address_from` DateTime,
    `address_type_code` String,
    `date_address_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `premise_id`, `date_address_from`, `address_type_code`);

CREATE TABLE `customers_campaigns_ecommerce`.`Customer_Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `order_status_code` String,
    `shipping_method_code` String,
    `order_placed_datetime` DateTime,
    `order_delivered_datetime` Nullable(DateTime),
    `order_shipping_charges` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `customers_campaigns_ecommerce`.`Mailshot_Customers` (
    `mailshot_id` Int64,
    `customer_id` Int64,
    `outcome_code` String,
    `mailshot_customer_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`mailshot_id`, `customer_id`, `outcome_code`);

CREATE TABLE `customers_campaigns_ecommerce`.`Order_Items` (
    `item_id` Int64,
    `order_item_status_code` String,
    `order_id` Int64,
    `product_id` Int64,
    `item_status_code` Nullable(String),
    `item_delivered_datetime` Nullable(DateTime),
    `item_order_quantity` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`item_id`, `order_item_status_code`, `order_id`, `product_id`);

