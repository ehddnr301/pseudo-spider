-- ClickHouse DDL for database: candidate_poll
-- Generated from: spider_data/database/candidate_poll/candidate_poll.sqlite

CREATE DATABASE IF NOT EXISTS candidate_poll;

CREATE TABLE `candidate_poll`.`candidate` (
    `Candidate_ID` Int32,
    `People_ID` Nullable(Int32),
    `Poll_Source` Nullable(String),
    `Date` Nullable(String),
    `Support_rate` Nullable(Float64),
    `Consider_rate` Nullable(Float64),
    `Oppose_rate` Nullable(Float64),
    `Unsure_rate` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Candidate_ID`;

CREATE TABLE `candidate_poll`.`people` (
    `People_ID` Int32,
    `Sex` Nullable(String),
    `Name` Nullable(String),
    `Date_of_Birth` Nullable(String),
    `Height` Nullable(Float64),
    `Weight` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

