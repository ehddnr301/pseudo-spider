-- ClickHouse DDL for database: driving_school
-- Generated from: spider_data/database/driving_school/driving_school.sqlite

CREATE DATABASE IF NOT EXISTS driving_school;

CREATE TABLE `driving_school`.`Addresses` (
    `address_id` Int64,
    `line_1_number_building` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `driving_school`.`Staff` (
    `staff_id` Int64,
    `staff_address_id` Int64,
    `nickname` Nullable(String),
    `first_name` Nullable(String),
    `middle_name` Nullable(String),
    `last_name` Nullable(String),
    `date_of_birth` Nullable(DateTime),
    `date_joined_staff` Nullable(DateTime),
    `date_left_staff` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `driving_school`.`Vehicles` (
    `vehicle_id` Int64,
    `vehicle_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `vehicle_id`;

CREATE TABLE `driving_school`.`Customers` (
    `customer_id` Int64,
    `customer_address_id` Int64,
    `customer_status_code` String,
    `date_became_customer` Nullable(DateTime),
    `date_of_birth` Nullable(DateTime),
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `amount_outstanding` Nullable(Float64),
    `email_address` Nullable(String),
    `phone_number` Nullable(String),
    `cell_mobile_phone_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `driving_school`.`Customer_Payments` (
    `customer_id` Int64,
    `datetime_payment` DateTime,
    `payment_method_code` String,
    `amount_payment` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`customer_id`, `datetime_payment`);

CREATE TABLE `driving_school`.`Lessons` (
    `lesson_id` Int64,
    `customer_id` Int64,
    `lesson_status_code` String,
    `staff_id` Nullable(Int64),
    `vehicle_id` Int64,
    `lesson_date` Nullable(DateTime),
    `lesson_time` Nullable(String),
    `price` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `lesson_id`;

