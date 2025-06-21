-- ClickHouse DDL for database: insurance_and_eClaims
-- Generated from: spider_data/database/insurance_and_eClaims/insurance_and_eClaims.sqlite

CREATE DATABASE IF NOT EXISTS insurance_and_eClaims;

CREATE TABLE `insurance_and_eClaims`.`Customers` (
    `Customer_ID` Int64,
    `Customer_Details` String
)
ENGINE = MergeTree()
ORDER BY `Customer_ID`;

CREATE TABLE `insurance_and_eClaims`.`Staff` (
    `Staff_ID` Int64,
    `Staff_Details` String
)
ENGINE = MergeTree()
ORDER BY `Staff_ID`;

CREATE TABLE `insurance_and_eClaims`.`Policies` (
    `Policy_ID` Int64,
    `Customer_ID` Int64,
    `Policy_Type_Code` String,
    `Start_Date` Nullable(DateTime),
    `End_Date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `Policy_ID`;

CREATE TABLE `insurance_and_eClaims`.`Claim_Headers` (
    `Claim_Header_ID` Int64,
    `Claim_Status_Code` String,
    `Claim_Type_Code` String,
    `Policy_ID` Int64,
    `Date_of_Claim` Nullable(DateTime),
    `Date_of_Settlement` Nullable(DateTime),
    `Amount_Claimed` Nullable(Decimal64(2)),
    `Amount_Piad` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `Claim_Header_ID`;

CREATE TABLE `insurance_and_eClaims`.`Claims_Documents` (
    `Claim_ID` Int64,
    `Document_Type_Code` String,
    `Created_by_Staff_ID` Nullable(Int64),
    `Created_Date` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`Claim_ID`, `Document_Type_Code`);

CREATE TABLE `insurance_and_eClaims`.`Claims_Processing_Stages` (
    `Claim_Stage_ID` Int64,
    `Next_Claim_Stage_ID` Nullable(Int64),
    `Claim_Status_Name` String,
    `Claim_Status_Description` String
)
ENGINE = MergeTree()
ORDER BY `Claim_Stage_ID`;

CREATE TABLE `insurance_and_eClaims`.`Claims_Processing` (
    `Claim_Processing_ID` Int64,
    `Claim_ID` Int64,
    `Claim_Outcome_Code` String,
    `Claim_Stage_ID` Int64,
    `Staff_ID` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Claim_Processing_ID`;

