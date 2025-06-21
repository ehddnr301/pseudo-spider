-- ClickHouse DDL for database: cinema
-- Generated from: spider_data/database/cinema/cinema.sqlite

CREATE DATABASE IF NOT EXISTS cinema;

CREATE TABLE `cinema`.`film` (
    `Film_ID` Int32,
    `Rank_in_series` Nullable(Int32),
    `Number_in_season` Nullable(Int32),
    `Title` Nullable(String),
    `Directed_by` Nullable(String),
    `Original_air_date` Nullable(String),
    `Production_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Film_ID`;

CREATE TABLE `cinema`.`cinema` (
    `Cinema_ID` Int32,
    `Name` Nullable(String),
    `Openning_year` Nullable(Int32),
    `Capacity` Nullable(Int32),
    `Location` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Cinema_ID`;

CREATE TABLE `cinema`.`schedule` (
    `Cinema_ID` Int32,
    `Film_ID` Int32,
    `Date` Nullable(String),
    `Show_times_per_day` Nullable(Int32),
    `Price` Nullable(Float32)
)
ENGINE = MergeTree()
ORDER BY (`Cinema_ID`, `Film_ID`);

