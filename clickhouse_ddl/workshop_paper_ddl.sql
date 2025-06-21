-- ClickHouse DDL for database: workshop_paper
-- Generated from: spider_data/database/workshop_paper/workshop_paper.sqlite

CREATE DATABASE IF NOT EXISTS workshop_paper;

CREATE TABLE `workshop_paper`.`workshop` (
    `Workshop_ID` Int32,
    `Date` Nullable(String),
    `Venue` Nullable(String),
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Workshop_ID`;

CREATE TABLE `workshop_paper`.`submission` (
    `Submission_ID` Int32,
    `Scores` Nullable(Float64),
    `Author` Nullable(String),
    `College` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Submission_ID`;

CREATE TABLE `workshop_paper`.`Acceptance` (
    `Submission_ID` Int32,
    `Workshop_ID` Int32,
    `Result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`Submission_ID`, `Workshop_ID`);

