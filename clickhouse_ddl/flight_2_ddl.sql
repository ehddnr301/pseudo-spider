-- ClickHouse DDL for database: flight_2
-- Generated from: spider_data/database/flight_2/flight_2.sqlite

CREATE DATABASE IF NOT EXISTS flight_2;

CREATE TABLE `flight_2`.`airlines` (
    `uid` Int64,
    `Airline` Nullable(String),
    `Abbreviation` Nullable(String),
    `Country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `uid`;

CREATE TABLE `flight_2`.`airports` (
    `City` Nullable(String),
    `AirportCode` String,
    `AirportName` Nullable(String),
    `Country` Nullable(String),
    `CountryAbbrev` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `AirportCode`;

CREATE TABLE `flight_2`.`flights` (
    `Airline` Int64,
    `FlightNo` Int64,
    `SourceAirport` Nullable(String),
    `DestAirport` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Airline`, `FlightNo`);

