-- ClickHouse DDL for database: farm
-- Generated from: spider_data/database/farm/farm.sqlite

CREATE DATABASE IF NOT EXISTS farm;

CREATE TABLE `farm`.`city` (
    `City_ID` Int32,
    `Official_Name` Nullable(String),
    `Status` Nullable(String),
    `Area_km_2` Nullable(Float64),
    `Population` Nullable(Float64),
    `Census_Ranking` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `City_ID`;

CREATE TABLE `farm`.`farm` (
    `Farm_ID` Int32,
    `Year` Nullable(Int32),
    `Total_Horses` Nullable(Float64),
    `Working_Horses` Nullable(Float64),
    `Total_Cattle` Nullable(Float64),
    `Oxen` Nullable(Float64),
    `Bulls` Nullable(Float64),
    `Cows` Nullable(Float64),
    `Pigs` Nullable(Float64),
    `Sheep_and_Goats` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Farm_ID`;

CREATE TABLE `farm`.`farm_competition` (
    `Competition_ID` Int32,
    `Year` Nullable(Int32),
    `Theme` Nullable(String),
    `Host_city_ID` Nullable(Int32),
    `Hosts` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Competition_ID`;

CREATE TABLE `farm`.`competition_record` (
    `Competition_ID` Int32,
    `Farm_ID` Int32,
    `Rank` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Competition_ID`, `Farm_ID`);

