-- ClickHouse DDL for database: party_host
-- Generated from: spider_data/database/party_host/party_host.sqlite

CREATE DATABASE IF NOT EXISTS party_host;

CREATE TABLE `party_host`.`party` (
    `Party_ID` Int32,
    `Party_Theme` Nullable(String),
    `Location` Nullable(String),
    `First_year` Nullable(String),
    `Last_year` Nullable(String),
    `Number_of_hosts` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Party_ID`;

CREATE TABLE `party_host`.`host` (
    `Host_ID` Int32,
    `Name` Nullable(String),
    `Nationality` Nullable(String),
    `Age` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Host_ID`;

CREATE TABLE `party_host`.`party_host` (
    `Party_ID` Int32,
    `Host_ID` Int32,
    `Is_Main_in_Charge` Nullable(UInt8)
)
ENGINE = MergeTree()
ORDER BY (`Party_ID`, `Host_ID`);

