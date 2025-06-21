-- ClickHouse DDL for database: hr_1
-- Generated from: spider_data/database/hr_1/hr_1.sqlite

CREATE DATABASE IF NOT EXISTS hr_1;

CREATE TABLE `hr_1`.`regions` (
    `REGION_ID` Decimal64(2),
    `REGION_NAME` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `REGION_ID`;

CREATE TABLE `hr_1`.`countries` (
    `COUNTRY_ID` String,
    `COUNTRY_NAME` Nullable(String),
    `REGION_ID` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `COUNTRY_ID`;

CREATE TABLE `hr_1`.`departments` (
    `DEPARTMENT_ID` Decimal64(2) DEFAULT '0',
    `DEPARTMENT_NAME` String,
    `MANAGER_ID` Nullable(Decimal64(2)),
    `LOCATION_ID` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `DEPARTMENT_ID`;

CREATE TABLE `hr_1`.`jobs` (
    `JOB_ID` String DEFAULT '',
    `JOB_TITLE` String,
    `MIN_SALARY` Nullable(Decimal64(2)),
    `MAX_SALARY` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `JOB_ID`;

CREATE TABLE `hr_1`.`employees` (
    `EMPLOYEE_ID` Decimal64(2) DEFAULT '0',
    `FIRST_NAME` Nullable(String),
    `LAST_NAME` String,
    `EMAIL` String,
    `PHONE_NUMBER` Nullable(String),
    `HIRE_DATE` Date,
    `JOB_ID` String,
    `SALARY` Nullable(Decimal64(2)),
    `COMMISSION_PCT` Nullable(Decimal64(2)),
    `MANAGER_ID` Nullable(Decimal64(2)),
    `DEPARTMENT_ID` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `EMPLOYEE_ID`;

CREATE TABLE `hr_1`.`job_history` (
    `EMPLOYEE_ID` Decimal64(2),
    `START_DATE` Date,
    `END_DATE` Date,
    `JOB_ID` String,
    `DEPARTMENT_ID` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY (`EMPLOYEE_ID`, `START_DATE`);

CREATE TABLE `hr_1`.`locations` (
    `LOCATION_ID` Decimal64(2) DEFAULT '0',
    `STREET_ADDRESS` Nullable(String),
    `POSTAL_CODE` Nullable(String),
    `CITY` String,
    `STATE_PROVINCE` Nullable(String),
    `COUNTRY_ID` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `LOCATION_ID`;

