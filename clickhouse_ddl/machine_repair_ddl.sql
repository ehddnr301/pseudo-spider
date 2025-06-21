-- ClickHouse DDL for database: machine_repair
-- Generated from: spider_data/database/machine_repair/machine_repair.sqlite

CREATE DATABASE IF NOT EXISTS machine_repair;

CREATE TABLE `machine_repair`.`repair` (
    `repair_ID` Int32,
    `name` Nullable(String),
    `Launch_Date` Nullable(String),
    `Notes` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `repair_ID`;

CREATE TABLE `machine_repair`.`machine` (
    `Machine_ID` Int32,
    `Making_Year` Nullable(Int32),
    `Class` Nullable(String),
    `Team` Nullable(String),
    `Machine_series` Nullable(String),
    `value_points` Nullable(Float64),
    `quality_rank` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Machine_ID`;

CREATE TABLE `machine_repair`.`technician` (
    `technician_id` Float64,
    `Name` Nullable(String),
    `Team` Nullable(String),
    `Starting_Year` Nullable(Float64),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `technician_id`;

CREATE TABLE `machine_repair`.`repair_assignment` (
    `technician_id` Int32,
    `repair_ID` Int32,
    `Machine_ID` Int32
)
ENGINE = MergeTree()
ORDER BY (`technician_id`, `repair_ID`, `Machine_ID`);

