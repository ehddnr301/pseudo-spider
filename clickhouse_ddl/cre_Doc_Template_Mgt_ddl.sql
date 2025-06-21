-- ClickHouse DDL for database: cre_Doc_Template_Mgt
-- Generated from: spider_data/database/cre_Doc_Template_Mgt/cre_Doc_Template_Mgt.sqlite

CREATE DATABASE IF NOT EXISTS cre_Doc_Template_Mgt;

CREATE TABLE `cre_Doc_Template_Mgt`.`Ref_Template_Types` (
    `Template_Type_Code` String,
    `Template_Type_Description` String
)
ENGINE = MergeTree()
ORDER BY `Template_Type_Code`;

CREATE TABLE `cre_Doc_Template_Mgt`.`Templates` (
    `Template_ID` Int64,
    `Version_Number` Int64,
    `Template_Type_Code` String,
    `Date_Effective_From` Nullable(DateTime),
    `Date_Effective_To` Nullable(DateTime),
    `Template_Details` String
)
ENGINE = MergeTree()
ORDER BY `Template_ID`;

CREATE TABLE `cre_Doc_Template_Mgt`.`Documents` (
    `Document_ID` Int64,
    `Template_ID` Nullable(Int64),
    `Document_Name` Nullable(String),
    `Document_Description` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

CREATE TABLE `cre_Doc_Template_Mgt`.`Paragraphs` (
    `Paragraph_ID` Int64,
    `Document_ID` Int64,
    `Paragraph_Text` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Paragraph_ID`;

