-- ClickHouse DDL for database: journal_committee
-- Generated from: spider_data/database/journal_committee/journal_committee.sqlite

CREATE DATABASE IF NOT EXISTS journal_committee;

CREATE TABLE `journal_committee`.`journal` (
    `Journal_ID` Int32,
    `Date` Nullable(String),
    `Theme` Nullable(String),
    `Sales` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Journal_ID`;

CREATE TABLE `journal_committee`.`editor` (
    `Editor_ID` Int32,
    `Name` Nullable(String),
    `Age` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Editor_ID`;

CREATE TABLE `journal_committee`.`journal_committee` (
    `Editor_ID` Int32,
    `Journal_ID` Int32,
    `Work_Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Editor_ID`, `Journal_ID`);

