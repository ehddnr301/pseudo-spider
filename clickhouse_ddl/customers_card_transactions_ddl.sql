-- ClickHouse DDL for database: customers_card_transactions
-- Generated from: spider_data/database/customers_card_transactions/customers_card_transactions.sqlite

CREATE DATABASE IF NOT EXISTS customers_card_transactions;

CREATE TABLE `customers_card_transactions`.`Accounts` (
    `account_id` Int64,
    `customer_id` Int64,
    `account_name` Nullable(String),
    `other_account_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `account_id`;

CREATE TABLE `customers_card_transactions`.`Customers` (
    `customer_id` Int64,
    `customer_first_name` Nullable(String),
    `customer_last_name` Nullable(String),
    `customer_address` Nullable(String),
    `customer_phone` Nullable(String),
    `customer_email` Nullable(String),
    `other_customer_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customers_card_transactions`.`Customers_Cards` (
    `card_id` Int64,
    `customer_id` Int64,
    `card_type_code` String,
    `card_number` Nullable(String),
    `date_valid_from` Nullable(DateTime),
    `date_valid_to` Nullable(DateTime),
    `other_card_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `card_id`;

CREATE TABLE `customers_card_transactions`.`Financial_Transactions` (
    `transaction_id` Int64,
    `previous_transaction_id` Nullable(Int64),
    `account_id` Int64,
    `card_id` Int64,
    `transaction_type` String,
    `transaction_date` Nullable(DateTime),
    `transaction_amount` Nullable(Float64),
    `transaction_comment` Nullable(String),
    `other_transaction_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`transaction_id`, `account_id`, `card_id`, `transaction_type`);

