-- ClickHouse DDL for database: train_station
-- Generated from: spider_data/database/train_station/train_station.sqlite

CREATE DATABASE IF NOT EXISTS train_station;

CREATE TABLE `train_station`.`station` (
    `Station_ID` Int32,
    `Name` Nullable(String),
    `Annual_entry_exit` Nullable(Float64),
    `Annual_interchanges` Nullable(Float64),
    `Total_Passengers` Nullable(Float64),
    `Location` Nullable(String),
    `Main_Services` Nullable(String),
    `Number_of_Platforms` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Station_ID`;

CREATE TABLE `train_station`.`train` (
    `Train_ID` Int32,
    `Name` Nullable(String),
    `Time` Nullable(String),
    `Service` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Train_ID`;

CREATE TABLE `train_station`.`train_station` (
    `Train_ID` Int32,
    `Station_ID` Int32
)
ENGINE = MergeTree()
ORDER BY (`Train_ID`, `Station_ID`);

