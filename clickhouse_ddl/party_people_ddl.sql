-- ClickHouse DDL for database: party_people
-- Generated from: spider_data/database/party_people/party_people.sqlite

CREATE DATABASE IF NOT EXISTS party_people;

CREATE TABLE `party_people`.`region` (
    `Region_ID` Int32,
    `Region_name` Nullable(String),
    `Date` Nullable(String),
    `Label` Nullable(String),
    `Format` Nullable(String),
    `Catalogue` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Region_ID`;

CREATE TABLE `party_people`.`party` (
    `Party_ID` Int32,
    `Minister` Nullable(String),
    `Took_office` Nullable(String),
    `Left_office` Nullable(String),
    `Region_ID` Nullable(Int32),
    `Party_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Party_ID`;

CREATE TABLE `party_people`.`member` (
    `Member_ID` Int32,
    `Member_Name` Nullable(String),
    `Party_ID` Nullable(String),
    `In_office` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `party_people`.`party_events` (
    `Event_ID` Int32,
    `Event_Name` Nullable(String),
    `Party_ID` Nullable(Int32),
    `Member_in_charge_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Event_ID`;

