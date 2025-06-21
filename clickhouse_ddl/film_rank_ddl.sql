-- ClickHouse DDL for database: film_rank
-- Generated from: spider_data/database/film_rank/film_rank.sqlite

CREATE DATABASE IF NOT EXISTS film_rank;

CREATE TABLE `film_rank`.`film` (
    `Film_ID` Int32,
    `Title` Nullable(String),
    `Studio` Nullable(String),
    `Director` Nullable(String),
    `Gross_in_dollar` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Film_ID`;

CREATE TABLE `film_rank`.`market` (
    `Market_ID` Int32,
    `Country` Nullable(String),
    `Number_cities` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Market_ID`;

CREATE TABLE `film_rank`.`film_market_estimation` (
    `Estimation_ID` Int32,
    `Low_Estimate` Nullable(Float64),
    `High_Estimate` Nullable(Float64),
    `Film_ID` Nullable(Int32),
    `Type` Nullable(String),
    `Market_ID` Nullable(Int32),
    `Year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Estimation_ID`;

