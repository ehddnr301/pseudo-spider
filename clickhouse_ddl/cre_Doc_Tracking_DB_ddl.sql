-- ClickHouse DDL for database: cre_Doc_Tracking_DB
-- Generated from: spider_data/database/cre_Doc_Tracking_DB/cre_Doc_Tracking_DB.sqlite

CREATE DATABASE IF NOT EXISTS cre_Doc_Tracking_DB;

CREATE TABLE `cre_Doc_Tracking_DB`.`Ref_Document_Types` (
    `Document_Type_Code` String,
    `Document_Type_Name` String,
    `Document_Type_Description` String
)
ENGINE = MergeTree()
ORDER BY `Document_Type_Code`;

CREATE TABLE `cre_Doc_Tracking_DB`.`Ref_Calendar` (
    `Calendar_Date` DateTime,
    `Day_Number` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Calendar_Date`;

CREATE TABLE `cre_Doc_Tracking_DB`.`Ref_Locations` (
    `Location_Code` String,
    `Location_Name` String,
    `Location_Description` String
)
ENGINE = MergeTree()
ORDER BY `Location_Code`;

CREATE TABLE `cre_Doc_Tracking_DB`.`Roles` (
    `Role_Code` String,
    `Role_Name` Nullable(String),
    `Role_Description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Role_Code`;

CREATE TABLE `cre_Doc_Tracking_DB`.`All_Documents` (
    `Document_ID` Int64,
    `Date_Stored` Nullable(DateTime),
    `Document_Type_Code` String,
    `Document_Name` Nullable(String),
    `Document_Description` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

CREATE TABLE `cre_Doc_Tracking_DB`.`Employees` (
    `Employee_ID` Int64,
    `Role_Code` String,
    `Employee_Name` Nullable(String),
    `Gender_MFU` String,
    `Date_of_Birth` DateTime,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Employee_ID`;

CREATE TABLE `cre_Doc_Tracking_DB`.`Document_Locations` (
    `Document_ID` Int64,
    `Location_Code` String,
    `Date_in_Location_From` DateTime,
    `Date_in_Locaton_To` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`Document_ID`, `Location_Code`, `Date_in_Location_From`);

CREATE TABLE `cre_Doc_Tracking_DB`.`Documents_to_be_Destroyed` (
    `Document_ID` Int64,
    `Destruction_Authorised_by_Employee_ID` Nullable(Int64),
    `Destroyed_by_Employee_ID` Nullable(Int64),
    `Planned_Destruction_Date` Nullable(DateTime),
    `Actual_Destruction_Date` Nullable(DateTime),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

