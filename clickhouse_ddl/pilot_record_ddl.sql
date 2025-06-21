-- ClickHouse DDL for database: pilot_record
-- Generated from: spider_data/database/pilot_record/pilot_record.sqlite

CREATE DATABASE IF NOT EXISTS pilot_record;

CREATE TABLE `pilot_record`.`aircraft` (
    `Aircraft_ID` Int32,
    `Order_Year` Nullable(Int32),
    `Manufacturer` Nullable(String),
    `Model` Nullable(String),
    `Fleet_Series` Nullable(String),
    `Powertrain` Nullable(String),
    `Fuel_Propulsion` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Aircraft_ID`;

CREATE TABLE `pilot_record`.`pilot` (
    `Pilot_ID` Int32,
    `Pilot_name` Nullable(String),
    `Rank` Nullable(Int32),
    `Age` Nullable(Int32),
    `Nationality` Nullable(String),
    `Position` Nullable(String),
    `Join_Year` Nullable(Int32),
    `Team` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Pilot_ID`;

CREATE TABLE `pilot_record`.`pilot_record` (
    `Record_ID` Nullable(Int32),
    `Pilot_ID` Int32,
    `Aircraft_ID` Int32,
    `Date` String
)
ENGINE = MergeTree()
ORDER BY (`Pilot_ID`, `Aircraft_ID`, `Date`);

