-- ClickHouse DDL for database: customer_deliveries
-- Generated from: spider_data/database/customer_deliveries/customer_deliveries.sqlite

CREATE DATABASE IF NOT EXISTS customer_deliveries;

CREATE TABLE `customer_deliveries`.`Products` (
    `product_id` Int64,
    `product_name` Nullable(String),
    `product_price` Nullable(Decimal64(2)),
    `product_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `customer_deliveries`.`Addresses` (
    `address_id` Int64,
    `address_details` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `customer_deliveries`.`Customers` (
    `customer_id` Int64,
    `payment_method` String,
    `customer_name` Nullable(String),
    `customer_phone` Nullable(String),
    `customer_email` Nullable(String),
    `date_became_customer` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `customer_deliveries`.`Regular_Orders` (
    `regular_order_id` Int64,
    `distributer_id` Int64
)
ENGINE = MergeTree()
ORDER BY `regular_order_id`;

CREATE TABLE `customer_deliveries`.`Regular_Order_Products` (
    `regular_order_id` Int64,
    `product_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`regular_order_id`, `product_id`);

CREATE TABLE `customer_deliveries`.`Actual_Orders` (
    `actual_order_id` Int64,
    `order_status_code` String,
    `regular_order_id` Int64,
    `actual_order_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `actual_order_id`;

CREATE TABLE `customer_deliveries`.`Actual_Order_Products` (
    `actual_order_id` Int64,
    `product_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`actual_order_id`, `product_id`);

CREATE TABLE `customer_deliveries`.`Customer_Addresses` (
    `customer_id` Int64,
    `address_id` Int64,
    `date_from` DateTime,
    `address_type` String,
    `date_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `address_id`, `date_from`, `address_type`);

CREATE TABLE `customer_deliveries`.`Delivery_Routes` (
    `route_id` Int64,
    `route_name` Nullable(String),
    `other_route_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `route_id`;

CREATE TABLE `customer_deliveries`.`Delivery_Route_Locations` (
    `location_code` String,
    `route_id` Int64,
    `location_address_id` Int64,
    `location_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `location_code`;

CREATE TABLE `customer_deliveries`.`Trucks` (
    `truck_id` Int64,
    `truck_licence_number` Nullable(String),
    `truck_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `truck_id`;

CREATE TABLE `customer_deliveries`.`Employees` (
    `employee_id` Int64,
    `employee_address_id` Int64,
    `employee_name` Nullable(String),
    `employee_phone` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `employee_id`;

CREATE TABLE `customer_deliveries`.`Order_Deliveries` (
    `location_code` String,
    `actual_order_id` Int64,
    `delivery_status_code` String,
    `driver_employee_id` Int64,
    `truck_id` Int64,
    `delivery_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`location_code`, `actual_order_id`, `delivery_status_code`, `driver_employee_id`, `truck_id`);

