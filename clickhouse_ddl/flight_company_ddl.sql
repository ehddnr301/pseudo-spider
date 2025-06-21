-- ClickHouse DDL for database: flight_company
-- Generated from: spider_data/database/flight_company/flight_company.sqlite

CREATE DATABASE IF NOT EXISTS flight_company;

CREATE TABLE `flight_company`.`airport` (
    `id` Int32,
    `City` Nullable(String),
    `Country` Nullable(String),
    `IATA` Nullable(String),
    `ICAO` Nullable(String),
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `flight_company`.`operate_company` (
    `id` Int32,
    `name` Nullable(String),
    `Type` Nullable(String),
    `Principal_activities` Nullable(String),
    `Incorporated_in` Nullable(String),
    `Group_Equity_Shareholding` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `flight_company`.`flight` (
    `id` Int32,
    `Vehicle_Flight_number` Nullable(String),
    `Date` Nullable(String),
    `Pilot` Nullable(String),
    `Velocity` Nullable(Float64),
    `Altitude` Nullable(Float64),
    `airport_id` Nullable(Int32),
    `company_id` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

