-- ClickHouse DDL for database: news_report
-- Generated from: spider_data/database/news_report/news_report.sqlite

CREATE DATABASE IF NOT EXISTS news_report;

CREATE TABLE `news_report`.`event` (
    `Event_ID` Int32,
    `Date` Nullable(String),
    `Venue` Nullable(String),
    `Name` Nullable(String),
    `Event_Attendance` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Event_ID`;

CREATE TABLE `news_report`.`journalist` (
    `journalist_ID` Int32,
    `Name` Nullable(String),
    `Nationality` Nullable(String),
    `Age` Nullable(String),
    `Years_working` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `journalist_ID`;

CREATE TABLE `news_report`.`news_report` (
    `journalist_ID` Int32,
    `Event_ID` Int32,
    `Work_Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`journalist_ID`, `Event_ID`);

