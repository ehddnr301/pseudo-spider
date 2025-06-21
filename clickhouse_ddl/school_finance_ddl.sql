-- ClickHouse DDL for database: school_finance
-- Generated from: spider_data/database/school_finance/school_finance.sqlite

CREATE DATABASE IF NOT EXISTS school_finance;

CREATE TABLE `school_finance`.`School` (
    `School_id` String,
    `School_name` Nullable(String),
    `Location` Nullable(String),
    `Mascot` Nullable(String),
    `Enrollment` Nullable(Int32),
    `IHSAA_Class` Nullable(String),
    `IHSAA_Football_Class` Nullable(String),
    `County` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `School_id`;

CREATE TABLE `school_finance`.`budget` (
    `School_id` Int32,
    `Year` Int32,
    `Budgeted` Nullable(Int32),
    `total_budget_percent_budgeted` Nullable(Float64),
    `Invested` Nullable(Int32),
    `total_budget_percent_invested` Nullable(Float64),
    `Budget_invested_percent` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`School_id`, `Year`);

CREATE TABLE `school_finance`.`endowment` (
    `endowment_id` Int32,
    `School_id` Nullable(Int32),
    `donator_name` Nullable(String),
    `amount` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `endowment_id`;

