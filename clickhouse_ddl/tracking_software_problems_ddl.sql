-- ClickHouse DDL for database: tracking_software_problems
-- Generated from: spider_data/database/tracking_software_problems/tracking_software_problems.sqlite

CREATE DATABASE IF NOT EXISTS tracking_software_problems;

CREATE TABLE `tracking_software_problems`.`Problem_Category_Codes` (
    `problem_category_code` String,
    `problem_category_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `problem_category_code`;

CREATE TABLE `tracking_software_problems`.`Problem_Log` (
    `problem_log_id` Int64,
    `assigned_to_staff_id` Int64,
    `problem_id` Int64,
    `problem_category_code` String,
    `problem_status_code` String,
    `log_entry_date` Nullable(DateTime),
    `log_entry_description` Nullable(String),
    `log_entry_fix` Nullable(String),
    `other_log_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `problem_log_id`;

CREATE TABLE `tracking_software_problems`.`Problem_Status_Codes` (
    `problem_status_code` String,
    `problem_status_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `problem_status_code`;

CREATE TABLE `tracking_software_problems`.`Product` (
    `product_id` Int64,
    `product_name` Nullable(String),
    `product_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `product_id`;

CREATE TABLE `tracking_software_problems`.`Staff` (
    `staff_id` Int64,
    `staff_first_name` Nullable(String),
    `staff_last_name` Nullable(String),
    `other_staff_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `tracking_software_problems`.`Problems` (
    `problem_id` Int64,
    `product_id` Int64,
    `closure_authorised_by_staff_id` Int64,
    `reported_by_staff_id` Int64,
    `date_problem_reported` DateTime,
    `date_problem_closed` Nullable(DateTime),
    `problem_description` Nullable(String),
    `other_problem_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `problem_id`;

