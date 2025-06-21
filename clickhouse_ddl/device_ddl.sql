-- ClickHouse DDL for database: device
-- Generated from: spider_data/database/device/device.sqlite

CREATE DATABASE IF NOT EXISTS device;

CREATE TABLE `device`.`device` (
    `Device_ID` Int32,
    `Device` Nullable(String),
    `Carrier` Nullable(String),
    `Package_Version` Nullable(String),
    `Applications` Nullable(String),
    `Software_Platform` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Device_ID`;

CREATE TABLE `device`.`shop` (
    `Shop_ID` Int32,
    `Shop_Name` Nullable(String),
    `Location` Nullable(String),
    `Open_Date` Nullable(String),
    `Open_Year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Shop_ID`;

CREATE TABLE `device`.`stock` (
    `Shop_ID` Int32,
    `Device_ID` Int32,
    `Quantity` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Shop_ID`, `Device_ID`);

