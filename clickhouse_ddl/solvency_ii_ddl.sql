-- ClickHouse DDL for database: solvency_ii
-- Generated from: spider_data/database/solvency_ii/solvency_ii.sqlite

CREATE DATABASE IF NOT EXISTS solvency_ii;

CREATE TABLE `solvency_ii`.`Addresses` (
    `Address_ID` Int64,
    `address_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Address_ID`;

CREATE TABLE `solvency_ii`.`Locations` (
    `Location_ID` Int64,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Location_ID`;

CREATE TABLE `solvency_ii`.`Products` (
    `Product_ID` Int64,
    `Product_Type_Code` Nullable(String),
    `Product_Name` Nullable(String),
    `Product_Price` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `Product_ID`;

CREATE TABLE `solvency_ii`.`Parties` (
    `Party_ID` Int64,
    `Party_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Party_ID`;

CREATE TABLE `solvency_ii`.`Assets` (
    `Asset_ID` Int64,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Asset_ID`;

CREATE TABLE `solvency_ii`.`Channels` (
    `Channel_ID` Int64,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Channel_ID`;

CREATE TABLE `solvency_ii`.`Finances` (
    `Finance_ID` Int64,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Finance_ID`;

CREATE TABLE `solvency_ii`.`Events` (
    `Event_ID` Int64,
    `Address_ID` Nullable(Int64),
    `Channel_ID` Int64,
    `Event_Type_Code` Nullable(String),
    `Finance_ID` Int64,
    `Location_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `Event_ID`;

CREATE TABLE `solvency_ii`.`Products_in_Events` (
    `Product_in_Event_ID` Int64,
    `Event_ID` Int64,
    `Product_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `Product_in_Event_ID`;

CREATE TABLE `solvency_ii`.`Parties_in_Events` (
    `Party_ID` Int64,
    `Event_ID` Int64,
    `Role_Code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Party_ID`, `Event_ID`);

CREATE TABLE `solvency_ii`.`Agreements` (
    `Document_ID` Int64,
    `Event_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `Document_ID`;

CREATE TABLE `solvency_ii`.`Assets_in_Events` (
    `Asset_ID` Int64,
    `Event_ID` Int64
)
ENGINE = MergeTree()
ORDER BY (`Asset_ID`, `Event_ID`);

