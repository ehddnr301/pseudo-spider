-- ClickHouse DDL for database: customers_and_invoices
-- Generated from: spider_data/database/customers_and_invoices/customers_and_invoices.sqlite

CREATE DATABASE IF NOT EXISTS customers_and_invoices;

CREATE TABLE `customers_and_invoices`.`Customers` (
    `customer_id` Int64,
    `customer_first_name` Nullable(String),
    `customer_middle_initial` Nullable(String),
    `customer_last_name` Nullable(String),
    `gender` Nullable(String),
    `email_address` Nullable(String),
    `login_name` Nullable(String),
    `login_password` Nullable(String),
    `phone_number` Nullable(String),
    `town_city` Nullable(String),
    `state_county_province` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customers_and_invoices`.`Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `date_order_placed` DateTime,
    `order_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `customers_and_invoices`.`Invoices` (
    `invoice_number` Int64,
    `order_id` Int64,
    `invoice_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `invoice_number`;

CREATE TABLE `customers_and_invoices`.`Accounts` (
    `account_id` Int64,
    `customer_id` Int64,
    `date_account_opened` Nullable(DateTime),
    `account_name` Nullable(String),
    `other_account_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `account_id`;

CREATE TABLE `customers_and_invoices`.`Product_Categories` (
    `production_type_code` String,
    `product_type_description` Nullable(String),
    `vat_rating` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `production_type_code`;

CREATE TABLE `customers_and_invoices`.`Products` (
    `product_id` Int64,
    `parent_product_id` Nullable(Int64),
    `production_type_code` String,
    `unit_price` Nullable(Decimal64(2)),
    `product_name` Nullable(String),
    `product_color` Nullable(String),
    `product_size` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customers_and_invoices`.`Financial_Transactions` (
    `transaction_id` Int64,
    `account_id` Int64,
    `invoice_number` Nullable(Int64),
    `transaction_type` String,
    `transaction_date` Nullable(DateTime),
    `transaction_amount` Nullable(Decimal64(2)),
    `transaction_comment` Nullable(String),
    `other_transaction_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`transaction_id`, `account_id`, `transaction_type`);

CREATE TABLE `customers_and_invoices`.`Order_Items` (
    `order_item_id` Int64,
    `order_id` Int64,
    `product_id` Int64,
    `product_quantity` Nullable(String),
    `other_order_item_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_item_id`;

CREATE TABLE `customers_and_invoices`.`Invoice_Line_Items` (
    `order_item_id` Int64,
    `invoice_number` Int64,
    `product_id` Int64,
    `product_title` Nullable(String),
    `product_quantity` Nullable(String),
    `product_price` Nullable(Decimal64(2)),
    `derived_product_cost` Nullable(Decimal64(2)),
    `derived_vat_payable` Nullable(Decimal64(2)),
    `derived_total_cost` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY (`order_item_id`, `invoice_number`, `product_id`);

