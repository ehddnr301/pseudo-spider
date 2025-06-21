-- ClickHouse DDL for database: aircraft
-- Generated from: spider_data/database/aircraft/aircraft.sqlite

CREATE DATABASE IF NOT EXISTS aircraft;

CREATE TABLE `aircraft`.`pilot` (
    `Pilot_Id` Int32,
    `Name` String,
    `Age` Int32
)
ENGINE = MergeTree()
ORDER BY `Pilot_Id`;

CREATE TABLE `aircraft`.`aircraft` (
    `Aircraft_ID` Int32,
    `Aircraft` String,
    `Description` String,
    `Max_Gross_Weight` String,
    `Total_disk_area` String,
    `Max_disk_Loading` String
)
ENGINE = MergeTree()
ORDER BY `Aircraft_ID`;

CREATE TABLE `aircraft`.`match` (
    `Round` Float64,
    `Location` Nullable(String),
    `Country` Nullable(String),
    `Date` Nullable(String),
    `Fastest_Qualifying` Nullable(String),
    `Winning_Pilot` Nullable(String),
    `Winning_Aircraft` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Round`;

CREATE TABLE `aircraft`.`airport` (
    `Airport_ID` Int32,
    `Airport_Name` Nullable(String),
    `Total_Passengers` Nullable(Float64),
    `%_Change_2007` Nullable(String),
    `International_Passengers` Nullable(Float64),
    `Domestic_Passengers` Nullable(Float64),
    `Transit_Passengers` Nullable(Float64),
    `Aircraft_Movements` Nullable(Float64),
    `Freight_Metric_Tonnes` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Airport_ID`;

CREATE TABLE `aircraft`.`airport_aircraft` (
    `ID` Nullable(Int32),
    `Airport_ID` Int32,
    `Aircraft_ID` Int32
)
ENGINE = MergeTree()
ORDER BY (`Airport_ID`, `Aircraft_ID`);

