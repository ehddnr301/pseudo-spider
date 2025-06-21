-- ClickHouse DDL for database: gas_company
-- Generated from: spider_data/database/gas_company/gas_company.sqlite

CREATE DATABASE IF NOT EXISTS gas_company;

CREATE TABLE `gas_company`.`company` (
    `Company_ID` Int32,
    `Rank` Nullable(Int32),
    `Company` Nullable(String),
    `Headquarters` Nullable(String),
    `Main_Industry` Nullable(String),
    `Sales_billion` Nullable(Float64),
    `Profits_billion` Nullable(Float64),
    `Assets_billion` Nullable(Float64),
    `Market_Value` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Company_ID`;

CREATE TABLE `gas_company`.`gas_station` (
    `Station_ID` Int32,
    `Open_Year` Nullable(Int32),
    `Location` Nullable(String),
    `Manager_Name` Nullable(String),
    `Vice_Manager_Name` Nullable(String),
    `Representative_Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Station_ID`;

CREATE TABLE `gas_company`.`station_company` (
    `Station_ID` Int32,
    `Company_ID` Int32,
    `Rank_of_the_Year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Station_ID`, `Company_ID`);

