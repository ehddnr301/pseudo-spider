-- ClickHouse DDL for database: museum_visit
-- Generated from: spider_data/database/museum_visit/museum_visit.sqlite

CREATE DATABASE IF NOT EXISTS museum_visit;

CREATE TABLE `museum_visit`.`museum` (
    `Museum_ID` Int32,
    `Name` Nullable(String),
    `Num_of_Staff` Nullable(Int32),
    `Open_Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Museum_ID`;

CREATE TABLE `museum_visit`.`visitor` (
    `ID` Int32,
    `Name` Nullable(String),
    `Level_of_membership` Nullable(Int32),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `museum_visit`.`visit` (
    `Museum_ID` Int32,
    `visitor_ID` String,
    `Num_of_Ticket` Nullable(Int32),
    `Total_spent` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Museum_ID`, `visitor_ID`);

