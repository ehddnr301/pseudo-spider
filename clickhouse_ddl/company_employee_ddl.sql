-- ClickHouse DDL for database: company_employee
-- Generated from: spider_data/database/company_employee/company_employee.sqlite

CREATE DATABASE IF NOT EXISTS company_employee;

CREATE TABLE `company_employee`.`people` (
    `People_ID` Int32,
    `Age` Nullable(Int32),
    `Name` Nullable(String),
    `Nationality` Nullable(String),
    `Graduation_College` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

CREATE TABLE `company_employee`.`company` (
    `Company_ID` Float64,
    `Name` Nullable(String),
    `Headquarters` Nullable(String),
    `Industry` Nullable(String),
    `Sales_in_Billion` Nullable(Float64),
    `Profits_in_Billion` Nullable(Float64),
    `Assets_in_Billion` Nullable(Float64),
    `Market_Value_in_Billion` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Company_ID`;

CREATE TABLE `company_employee`.`employment` (
    `Company_ID` Int32,
    `People_ID` Int32,
    `Year_working` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Company_ID`, `People_ID`);

