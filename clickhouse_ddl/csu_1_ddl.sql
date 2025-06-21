-- ClickHouse DDL for database: csu_1
-- Generated from: spider_data/database/csu_1/csu_1.sqlite

CREATE DATABASE IF NOT EXISTS csu_1;

CREATE TABLE `csu_1`.`Campuses` (
    `Id` Int64,
    `Campus` Nullable(String),
    `Location` Nullable(String),
    `County` Nullable(String),
    `Year` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Id`;

CREATE TABLE `csu_1`.`csu_fees` (
    `Campus` Int64,
    `Year` Nullable(Int64),
    `CampusFee` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Campus`;

CREATE TABLE `csu_1`.`degrees` (
    `Year` Int64,
    `Campus` Int64,
    `Degrees` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`Year`, `Campus`);

CREATE TABLE `csu_1`.`discipline_enrollments` (
    `Campus` Int64,
    `Discipline` Int64,
    `Year` Nullable(Int64),
    `Undergraduate` Nullable(Int64),
    `Graduate` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`Campus`, `Discipline`);

CREATE TABLE `csu_1`.`enrollments` (
    `Campus` Int64,
    `Year` Int64,
    `TotalEnrollment_AY` Nullable(Int64),
    `FTE_AY` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`Campus`, `Year`);

CREATE TABLE `csu_1`.`faculty` (
    `Campus` Nullable(Int64),
    `Year` Nullable(Int64),
    `Faculty` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY tuple();

