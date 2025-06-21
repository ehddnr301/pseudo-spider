-- ClickHouse DDL for database: cre_Docs_and_Epenses
-- Generated from: spider_data/database/cre_Docs_and_Epenses/cre_Docs_and_Epenses.sqlite

CREATE DATABASE IF NOT EXISTS cre_Docs_and_Epenses;

CREATE TABLE `cre_Docs_and_Epenses`.`Ref_Document_Types` (
    `Document_Type_Code` String,
    `Document_Type_Name` String,
    `Document_Type_Description` String
)
ENGINE = MergeTree()
ORDER BY `Document_Type_Code`;

CREATE TABLE `cre_Docs_and_Epenses`.`Ref_Budget_Codes` (
    `Budget_Type_Code` String,
    `Budget_Type_Description` String
)
ENGINE = MergeTree()
ORDER BY `Budget_Type_Code`;

CREATE TABLE `cre_Docs_and_Epenses`.`Projects` (
    `Project_ID` Int64,
    `Project_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Project_ID`;

CREATE TABLE `cre_Docs_and_Epenses`.`Documents` (
    `Document_ID` Int64,
    `Document_Type_Code` String,
    `Project_ID` Int64,
    `Document_Date` Nullable(DateTime),
    `Document_Name` Nullable(String),
    `Document_Description` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

CREATE TABLE `cre_Docs_and_Epenses`.`Statements` (
    `Statement_ID` Int64,
    `Statement_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Statement_ID`;

CREATE TABLE `cre_Docs_and_Epenses`.`Documents_with_Expenses` (
    `Document_ID` Int64,
    `Budget_Type_Code` String,
    `Document_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

CREATE TABLE `cre_Docs_and_Epenses`.`Accounts` (
    `Account_ID` Int64,
    `Statement_ID` Int64,
    `Account_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Account_ID`;

