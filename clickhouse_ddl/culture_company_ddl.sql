-- ClickHouse DDL for database: culture_company
-- Generated from: spider_data/database/culture_company/culture_company.sqlite

CREATE DATABASE IF NOT EXISTS culture_company;

CREATE TABLE `culture_company`.`book_club` (
    `book_club_id` Int32,
    `Year` Nullable(Int32),
    `Author_or_Editor` Nullable(String),
    `Book_Title` Nullable(String),
    `Publisher` Nullable(String),
    `Category` Nullable(String),
    `Result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `book_club_id`;

CREATE TABLE `culture_company`.`movie` (
    `movie_id` Int32,
    `Title` Nullable(String),
    `Year` Nullable(Int32),
    `Director` Nullable(String),
    `Budget_million` Nullable(Float64),
    `Gross_worldwide` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `movie_id`;

CREATE TABLE `culture_company`.`culture_company` (
    `Company_name` String,
    `Type` Nullable(String),
    `Incorporated_in` Nullable(String),
    `Group_Equity_Shareholding` Nullable(Float64),
    `book_club_id` Nullable(String),
    `movie_id` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Company_name`;

