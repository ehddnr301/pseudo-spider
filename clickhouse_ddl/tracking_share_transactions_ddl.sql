-- ClickHouse DDL for database: tracking_share_transactions
-- Generated from: spider_data/database/tracking_share_transactions/tracking_share_transactions.sqlite

CREATE DATABASE IF NOT EXISTS tracking_share_transactions;

CREATE TABLE `tracking_share_transactions`.`Investors` (
    `investor_id` Int64,
    `Investor_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `investor_id`;

CREATE TABLE `tracking_share_transactions`.`Lots` (
    `lot_id` Int64,
    `investor_id` Int64,
    `lot_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `lot_id`;

CREATE TABLE `tracking_share_transactions`.`Ref_Transaction_Types` (
    `transaction_type_code` String,
    `transaction_type_description` String
)
ENGINE = MergeTree()
ORDER BY `transaction_type_code`;

CREATE TABLE `tracking_share_transactions`.`Transactions` (
    `transaction_id` Int64,
    `investor_id` Int64,
    `transaction_type_code` String,
    `date_of_transaction` Nullable(DateTime),
    `amount_of_transaction` Nullable(Decimal64(2)),
    `share_count` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `transaction_id`;

CREATE TABLE `tracking_share_transactions`.`Sales` (
    `sales_transaction_id` Int64,
    `sales_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `sales_transaction_id`;

CREATE TABLE `tracking_share_transactions`.`Purchases` (
    `purchase_transaction_id` Int64,
    `purchase_details` String
)
ENGINE = MergeTree()
ORDER BY (`purchase_transaction_id`, `purchase_details`);

CREATE TABLE `tracking_share_transactions`.`Transactions_Lots` (
    `transaction_id` Int64,
    `lot_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`transaction_id`, `lot_id`);

