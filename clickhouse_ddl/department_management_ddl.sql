-- ClickHouse DDL for database: department_management
-- Generated from: spider_data/database/department_management/department_management.sqlite

CREATE DATABASE IF NOT EXISTS department_management;

CREATE TABLE `department_management`.`department` (
    `Department_ID` Int32,
    `Name` Nullable(String),
    `Creation` Nullable(String),
    `Ranking` Nullable(Int32),
    `Budget_in_Billions` Nullable(Float64),
    `Num_Employees` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Department_ID`;

CREATE TABLE `department_management`.`head` (
    `head_ID` Int32,
    `name` Nullable(String),
    `born_state` Nullable(String),
    `age` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `head_ID`;

CREATE TABLE `department_management`.`management` (
    `department_ID` Int32,
    `head_ID` Int32,
    `temporary_acting` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`department_ID`, `head_ID`);

