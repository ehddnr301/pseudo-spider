-- ClickHouse DDL for database: loan_1
-- Generated from: spider_data/database/loan_1/loan_1.sqlite

CREATE DATABASE IF NOT EXISTS loan_1;

CREATE TABLE `loan_1`.`bank` (
    `branch_ID` Int32,
    `bname` Nullable(String),
    `no_of_customers` Nullable(Int32),
    `city` Nullable(String),
    `state` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `branch_ID`;

CREATE TABLE `loan_1`.`customer` (
    `cust_ID` String,
    `cust_name` Nullable(String),
    `acc_type` Nullable(String),
    `acc_bal` Nullable(Int32),
    `no_of_loans` Nullable(Int32),
    `credit_score` Nullable(Int32),
    `branch_ID` Nullable(Int32),
    `state` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `cust_ID`;

CREATE TABLE `loan_1`.`loan` (
    `loan_ID` String,
    `loan_type` Nullable(String),
    `cust_ID` Nullable(String),
    `branch_ID` Nullable(String),
    `amount` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `loan_ID`;

