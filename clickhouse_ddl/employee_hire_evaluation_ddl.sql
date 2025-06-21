-- ClickHouse DDL for database: employee_hire_evaluation
-- Generated from: spider_data/database/employee_hire_evaluation/employee_hire_evaluation.sqlite

CREATE DATABASE IF NOT EXISTS employee_hire_evaluation;

CREATE TABLE `employee_hire_evaluation`.`employee` (
    `Employee_ID` Int32,
    `Name` Nullable(String),
    `Age` Nullable(Int32),
    `City` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Employee_ID`;

CREATE TABLE `employee_hire_evaluation`.`shop` (
    `Shop_ID` Int32,
    `Name` Nullable(String),
    `Location` Nullable(String),
    `District` Nullable(String),
    `Number_products` Nullable(Int32),
    `Manager_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Shop_ID`;

CREATE TABLE `employee_hire_evaluation`.`hiring` (
    `Shop_ID` Nullable(Int32),
    `Employee_ID` Int32,
    `Start_from` Nullable(String),
    `Is_full_time` Nullable(UInt8)
)
ENGINE = MergeTree()
ORDER BY `Employee_ID`;

CREATE TABLE `employee_hire_evaluation`.`evaluation` (
    `Employee_ID` String,
    `Year_awarded` String,
    `Bonus` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Employee_ID`, `Year_awarded`);

