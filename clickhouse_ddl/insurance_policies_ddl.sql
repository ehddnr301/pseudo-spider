-- ClickHouse DDL for database: insurance_policies
-- Generated from: spider_data/database/insurance_policies/insurance_policies.sqlite

CREATE DATABASE IF NOT EXISTS insurance_policies;

CREATE TABLE `insurance_policies`.`Customers` (
    `Customer_ID` Int64,
    `Customer_Details` String
)
ENGINE = MergeTree()
ORDER BY `Customer_ID`;

CREATE TABLE `insurance_policies`.`Customer_Policies` (
    `Policy_ID` Int64,
    `Customer_ID` Int64,
    `Policy_Type_Code` String,
    `Start_Date` Nullable(Date),
    `End_Date` Nullable(Date)
)
ENGINE = MergeTree()
ORDER BY `Policy_ID`;

CREATE TABLE `insurance_policies`.`Claims` (
    `Claim_ID` Int64,
    `Policy_ID` Int64,
    `Date_Claim_Made` Nullable(Date),
    `Date_Claim_Settled` Nullable(Date),
    `Amount_Claimed` Nullable(Int64),
    `Amount_Settled` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Claim_ID`;

CREATE TABLE `insurance_policies`.`Settlements` (
    `Settlement_ID` Int64,
    `Claim_ID` Int64,
    `Date_Claim_Made` Nullable(Date),
    `Date_Claim_Settled` Nullable(Date),
    `Amount_Claimed` Nullable(Int64),
    `Amount_Settled` Nullable(Int64),
    `Customer_Policy_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `Settlement_ID`;

CREATE TABLE `insurance_policies`.`Payments` (
    `Payment_ID` Int64,
    `Settlement_ID` Int64,
    `Payment_Method_Code` Nullable(String),
    `Date_Payment_Made` Nullable(Date),
    `Amount_Payment` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Payment_ID`;

