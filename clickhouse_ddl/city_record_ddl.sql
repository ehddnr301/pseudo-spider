-- ClickHouse DDL for database: city_record
-- Generated from: spider_data/database/city_record/city_record.sqlite

CREATE DATABASE IF NOT EXISTS city_record;

CREATE TABLE `city_record`.`city` (
    `City_ID` Int32,
    `City` Nullable(String),
    `Hanzi` Nullable(String),
    `Hanyu_Pinyin` Nullable(String),
    `Regional_Population` Nullable(Int32),
    `GDP` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `City_ID`;

CREATE TABLE `city_record`.`match` (
    `Match_ID` Int32,
    `Date` Nullable(String),
    `Venue` Nullable(String),
    `Score` Nullable(String),
    `Result` Nullable(String),
    `Competition` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Match_ID`;

CREATE TABLE `city_record`.`temperature` (
    `City_ID` Int32,
    `Jan` Nullable(Float64),
    `Feb` Nullable(Float64),
    `Mar` Nullable(Float64),
    `Apr` Nullable(Float64),
    `Jun` Nullable(Float64),
    `Jul` Nullable(Float64),
    `Aug` Nullable(Float64),
    `Sep` Nullable(Float64),
    `Oct` Nullable(Float64),
    `Nov` Nullable(Float64),
    `Dec` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `City_ID`;

CREATE TABLE `city_record`.`hosting_city` (
    `Year` Int32,
    `Match_ID` Nullable(Int32),
    `Host_City` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Year`;

