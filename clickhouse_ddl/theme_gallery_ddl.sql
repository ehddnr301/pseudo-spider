-- ClickHouse DDL for database: theme_gallery
-- Generated from: spider_data/database/theme_gallery/theme_gallery.sqlite

CREATE DATABASE IF NOT EXISTS theme_gallery;

CREATE TABLE `theme_gallery`.`artist` (
    `Artist_ID` Int32,
    `Name` Nullable(String),
    `Country` Nullable(String),
    `Year_Join` Nullable(Int32),
    `Age` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Artist_ID`;

CREATE TABLE `theme_gallery`.`exhibition` (
    `Exhibition_ID` Int32,
    `Year` Nullable(Int32),
    `Theme` Nullable(String),
    `Artist_ID` Nullable(Int32),
    `Ticket_Price` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Exhibition_ID`;

CREATE TABLE `theme_gallery`.`exhibition_record` (
    `Exhibition_ID` Int32,
    `Date` String,
    `Attendance` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Exhibition_ID`, `Date`);

