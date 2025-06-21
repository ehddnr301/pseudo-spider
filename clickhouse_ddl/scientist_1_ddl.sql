-- ClickHouse DDL for database: scientist_1
-- Generated from: spider_data/database/scientist_1/scientist_1.sqlite

CREATE DATABASE IF NOT EXISTS scientist_1;

CREATE TABLE `scientist_1`.`Scientists` (
    `SSN` Int32,
    `Name` String
)
ENGINE = MergeTree()
ORDER BY `SSN`;

CREATE TABLE `scientist_1`.`Projects` (
    `Code` String,
    `Name` String,
    `Hours` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Code`;

CREATE TABLE `scientist_1`.`AssignedTo` (
    `Scientist` Int32,
    `Project` String
)
ENGINE = MergeTree()
ORDER BY (`Scientist`, `Project`);

