-- ClickHouse DDL for database: company_1
-- Generated from: spider_data/database/company_1/company_1.sqlite

CREATE DATABASE IF NOT EXISTS company_1;

CREATE TABLE `company_1`.`works_on` (
    `Essn` Int64,
    `Pno` Int64,
    `Hours` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Essn`, `Pno`);

CREATE TABLE `company_1`.`employee` (
    `Fname` Nullable(String),
    `Minit` Nullable(String),
    `Lname` Nullable(String),
    `Ssn` Int64,
    `Bdate` Nullable(String),
    `Address` Nullable(String),
    `Sex` Nullable(String),
    `Salary` Nullable(Int64),
    `Super_ssn` Nullable(Int64),
    `Dno` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Ssn`;

CREATE TABLE `company_1`.`department` (
    `Dname` Nullable(String),
    `Dnumber` Int64,
    `Mgr_ssn` Nullable(Int64),
    `Mgr_start_date` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Dnumber`;

CREATE TABLE `company_1`.`project` (
    `Pname` Nullable(String),
    `Pnumber` Int64,
    `Plocation` Nullable(String),
    `Dnum` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Pnumber`;

CREATE TABLE `company_1`.`dependent` (
    `Essn` Int64,
    `Dependent_name` String,
    `Sex` Nullable(String),
    `Bdate` Nullable(String),
    `Relationship` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Essn`, `Dependent_name`);

CREATE TABLE `company_1`.`dept_locations` (
    `Dnumber` Int64,
    `Dlocation` String
)
ENGINE = MergeTree()
ORDER BY (`Dnumber`, `Dlocation`);

