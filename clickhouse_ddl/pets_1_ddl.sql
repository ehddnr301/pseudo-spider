-- ClickHouse DDL for database: pets_1
-- Generated from: spider_data/database/pets_1/pets_1.sqlite

CREATE DATABASE IF NOT EXISTS pets_1;

CREATE TABLE `pets_1`.`Student` (
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

CREATE TABLE `pets_1`.`Has_Pet` (
    `StuID` Nullable(Int64),
    `PetID` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `pets_1`.`Pets` (
    `PetID` Int64,
    `PetType` Nullable(String),
    `pet_age` Nullable(Int64),
    `weight` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `PetID`;

