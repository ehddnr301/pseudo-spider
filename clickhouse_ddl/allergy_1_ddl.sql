-- ClickHouse DDL for database: allergy_1
-- Generated from: spider_data/database/allergy_1/allergy_1.sqlite

CREATE DATABASE IF NOT EXISTS allergy_1;

CREATE TABLE `allergy_1`.`Allergy_Type` (
    `Allergy` String,
    `AllergyType` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Allergy`;

CREATE TABLE `allergy_1`.`Has_Allergy` (
    `StuID` Nullable(Int64),
    `Allergy` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `allergy_1`.`Student` (
    `StuID` Int64,
    `LName` Nullable(String),
    `Fname` Nullable(String),
    `Age` Nullable(Int64),
    `Sex` Nullable(String),
    `Major` Nullable(Int64),
    `Advisor` Nullable(Int64),
    `city_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `StuID`;

