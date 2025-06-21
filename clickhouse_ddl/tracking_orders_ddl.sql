-- ClickHouse DDL for database: tracking_orders
-- Generated from: spider_data/database/tracking_orders/tracking_orders.sqlite

CREATE DATABASE IF NOT EXISTS tracking_orders;

CREATE TABLE `tracking_orders`.`Customers` (
    `customer_id` Int64,
    `customer_name` Nullable(String),
    `customer_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `tracking_orders`.`Invoices` (
    `invoice_number` Int64,
    `invoice_date` Nullable(DateTime),
    `invoice_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `invoice_number`;

CREATE TABLE `tracking_orders`.`Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `order_status` String,
    `date_order_placed` DateTime,
    `order_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `tracking_orders`.`Products` (
    `product_id` Int64,
    `product_name` Nullable(String),
    `product_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `tracking_orders`.`Order_Items` (
    `order_item_id` Int64,
    `product_id` Int64,
    `order_id` Int64,
    `order_item_status` String,
    `order_item_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `order_item_id`;

CREATE TABLE `tracking_orders`.`Shipments` (
    `shipment_id` Int64,
    `order_id` Int64,
    `invoice_number` Int64,
    `shipment_tracking_number` Nullable(String),
    `shipment_date` Nullable(DateTime),
    `other_shipment_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `shipment_id`;

CREATE TABLE `tracking_orders`.`Shipment_Items` (
    `shipment_id` Int64,
    `order_item_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`shipment_id`, `order_item_id`);

