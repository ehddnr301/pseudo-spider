-- ClickHouse DDL for database: book_2
-- Generated from: spider_data/database/book_2/book_2.sqlite

CREATE DATABASE IF NOT EXISTS book_2;

CREATE TABLE `book_2`.`publication` (
    `Publication_ID` Int32,
    `Book_ID` Nullable(Int32),
    `Publisher` Nullable(String),
    `Publication_Date` Nullable(String),
    `Price` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Publication_ID`;

CREATE TABLE `book_2`.`book` (
    `Book_ID` Int32,
    `Title` Nullable(String),
    `Issues` Nullable(Float64),
    `Writer` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Book_ID`;

