-- ClickHouse DDL for database: insurance_fnol
-- Generated from: spider_data/database/insurance_fnol/insurance_fnol.sqlite

CREATE DATABASE IF NOT EXISTS insurance_fnol;

CREATE TABLE `insurance_fnol`.`Customers` (
    `Customer_ID` Int64,
    `Customer_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Customer_ID`;

CREATE TABLE `insurance_fnol`.`Services` (
    `Service_ID` Int64,
    `Service_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Service_ID`;

CREATE TABLE `insurance_fnol`.`Available_Policies` (
    `Policy_ID` Int64,
    `policy_type_code` Nullable(String),
    `Customer_Phone` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Policy_ID`;

CREATE TABLE `insurance_fnol`.`Customers_Policies` (
    `Customer_ID` Int64,
    `Policy_ID` Int64,
    `Date_Opened` Nullable(Date),
    `Date_Closed` Nullable(Date)
)
ENGINE = MergeTree()
ORDER BY (`Customer_ID`, `Policy_ID`);

CREATE TABLE `insurance_fnol`.`First_Notification_of_Loss` (
    `FNOL_ID` Int64,
    `Customer_ID` Int64,
    `Policy_ID` Int64,
    `Service_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `FNOL_ID`;

CREATE TABLE `insurance_fnol`.`Claims` (
    `Claim_ID` Int64,
    `FNOL_ID` Int64,
    `Effective_Date` Nullable(Date)
)
ENGINE = MergeTree()
ORDER BY `Claim_ID`;

CREATE TABLE `insurance_fnol`.`Settlements` (
    `Settlement_ID` Int64,
    `Claim_ID` Nullable(Int64),
    `Effective_Date` Nullable(Date),
    `Settlement_Amount` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Settlement_ID`;

