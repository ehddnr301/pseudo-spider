-- ClickHouse DDL for database: icfp_1
-- Generated from: spider_data/database/icfp_1/icfp_1.sqlite

CREATE DATABASE IF NOT EXISTS icfp_1;

CREATE TABLE `icfp_1`.`Inst` (
    `instID` Int64,
    `name` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `instID`;

CREATE TABLE `icfp_1`.`Authors` (
    `authID` Int64,
    `lname` Nullable(String),
    `fname` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `authID`;

CREATE TABLE `icfp_1`.`Papers` (
    `paperID` Int64,
    `title` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `paperID`;

CREATE TABLE `icfp_1`.`Authorship` (
    `authID` Int64,
    `instID` Int64,
    `paperID` Int64,
    `authOrder` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`authID`, `instID`, `paperID`);

