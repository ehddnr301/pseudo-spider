-- ClickHouse DDL for database: department_store
-- Generated from: spider_data/database/department_store/department_store.sqlite

CREATE DATABASE IF NOT EXISTS department_store;

CREATE TABLE `department_store`.`Addresses` (
    `address_id` Int64,
    `address_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `department_store`.`Staff` (
    `staff_id` Int64,
    `staff_gender` Nullable(String),
    `staff_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `department_store`.`Suppliers` (
    `supplier_id` Int64,
    `supplier_name` Nullable(String),
    `supplier_phone` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `supplier_id`;

CREATE TABLE `department_store`.`Department_Store_Chain` (
    `dept_store_chain_id` Int64,
    `dept_store_chain_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `dept_store_chain_id`;

CREATE TABLE `department_store`.`Customers` (
    `customer_id` Int64,
    `payment_method_code` String,
    `customer_code` Nullable(String),
    `customer_name` Nullable(String),
    `customer_address` Nullable(String),
    `customer_phone` Nullable(String),
    `customer_email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `department_store`.`Products` (
    `product_id` Int64,
    `product_type_code` String,
    `product_name` Nullable(String),
    `product_price` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `department_store`.`Supplier_Addresses` (
    `supplier_id` Int64,
    `address_id` Int64,
    `date_from` DateTime,
    `date_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`supplier_id`, `address_id`);

CREATE TABLE `department_store`.`Customer_Addresses` (
    `customer_id` Int64,
    `address_id` Int64,
    `date_from` DateTime,
    `date_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `address_id`);

CREATE TABLE `department_store`.`Customer_Orders` (
    `order_id` Int64,
    `customer_id` Int64,
    `order_status_code` String,
    `order_date` DateTime
)
ENGINE = MergeTree()
ORDER BY `order_id`;

CREATE TABLE `department_store`.`Department_Stores` (
    `dept_store_id` Int64,
    `dept_store_chain_id` Nullable(Int64),
    `store_name` Nullable(String),
    `store_address` Nullable(String),
    `store_phone` Nullable(String),
    `store_email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `dept_store_id`;

CREATE TABLE `department_store`.`Departments` (
    `department_id` Int64,
    `dept_store_id` Int64,
    `department_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `department_id`;

CREATE TABLE `department_store`.`Order_Items` (
    `order_item_id` Int64,
    `order_id` Int64,
    `product_id` Int64
)
ENGINE = MergeTree()
ORDER BY `order_item_id`;

CREATE TABLE `department_store`.`Product_Suppliers` (
    `product_id` Int64,
    `supplier_id` Int64,
    `date_supplied_from` DateTime,
    `date_supplied_to` Nullable(DateTime),
    `total_amount_purchased` Nullable(String),
    `total_value_purchased` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY (`product_id`, `supplier_id`);

CREATE TABLE `department_store`.`Staff_Department_Assignments` (
    `staff_id` Int64,
    `department_id` Int64,
    `date_assigned_from` DateTime,
    `job_title_code` String,
    `date_assigned_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`staff_id`, `department_id`);

