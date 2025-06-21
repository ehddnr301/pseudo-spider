-- ClickHouse DDL for database: election_representative
-- Generated from: spider_data/database/election_representative/election_representative.sqlite

CREATE DATABASE IF NOT EXISTS election_representative;

CREATE TABLE `election_representative`.`election` (
    `Election_ID` Int32,
    `Representative_ID` Nullable(Int32),
    `Date` Nullable(String),
    `Votes` Nullable(Float64),
    `Vote_Percent` Nullable(Float64),
    `Seats` Nullable(Float64),
    `Place` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Election_ID`;

CREATE TABLE `election_representative`.`representative` (
    `Representative_ID` Int32,
    `Name` Nullable(String),
    `State` Nullable(String),
    `Party` Nullable(String),
    `Lifespan` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Representative_ID`;

