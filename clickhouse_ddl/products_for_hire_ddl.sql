-- ClickHouse DDL for database: products_for_hire
-- Generated from: spider_data/database/products_for_hire/products_for_hire.sqlite

CREATE DATABASE IF NOT EXISTS products_for_hire;

CREATE TABLE `products_for_hire`.`Discount_Coupons` (
    `coupon_id` Int64,
    `date_issued` Nullable(DateTime),
    `coupon_amount` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `coupon_id`;

CREATE TABLE `products_for_hire`.`Customers` (
    `customer_id` Int64,
    `coupon_id` Int64,
    `good_or_bad_customer` Nullable(String),
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `gender_mf` Nullable(String),
    `date_became_customer` Nullable(DateTime),
    `date_last_hire` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `products_for_hire`.`Bookings` (
    `booking_id` Int64,
    `customer_id` Int64,
    `booking_status_code` String,
    `returned_damaged_yn` Nullable(String),
    `booking_start_date` Nullable(DateTime),
    `booking_end_date` Nullable(DateTime),
    `count_hired` Nullable(String),
    `amount_payable` Nullable(Decimal64(2)),
    `amount_of_discount` Nullable(Decimal64(2)),
    `amount_outstanding` Nullable(Decimal64(2)),
    `amount_of_refund` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `booking_id`;

CREATE TABLE `products_for_hire`.`Products_for_Hire` (
    `product_id` Int64,
    `product_type_code` String,
    `daily_hire_cost` Nullable(Decimal64(2)),
    `product_name` Nullable(String),
    `product_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `products_for_hire`.`Payments` (
    `payment_id` Int64,
    `booking_id` Nullable(Int64),
    `customer_id` Int64,
    `payment_type_code` String,
    `amount_paid_in_full_yn` Nullable(String),
    `payment_date` Nullable(DateTime),
    `amount_due` Nullable(Decimal64(2)),
    `amount_paid` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `payment_id`;

CREATE TABLE `products_for_hire`.`Products_Booked` (
    `booking_id` Int64,
    `product_id` Int64,
    `returned_yn` Nullable(String),
    `returned_late_yn` Nullable(String),
    `booked_count` Nullable(Int64),
    `booked_amount` Nullable(Float32)
)
ENGINE = MergeTree()
ORDER BY (`booking_id`, `product_id`);

CREATE TABLE `products_for_hire`.`View_Product_Availability` (
    `product_id` Int64,
    `booking_id` Int64,
    `status_date` DateTime,
    `available_yn` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `status_date`;

