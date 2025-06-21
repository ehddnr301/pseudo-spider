-- ClickHouse DDL for database: movie_1
-- Generated from: spider_data/database/movie_1/movie_1.sqlite

CREATE DATABASE IF NOT EXISTS movie_1;

CREATE TABLE `movie_1`.`Movie` (
    `mID` Int32,
    `title` Nullable(String),
    `year` Nullable(Int32),
    `director` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `mID`;

CREATE TABLE `movie_1`.`Reviewer` (
    `rID` Int32,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `rID`;

CREATE TABLE `movie_1`.`Rating` (
    `rID` Nullable(Int32),
    `mID` Nullable(Int32),
    `stars` Nullable(Int32),
    `ratingDate` Nullable(Date)
)
ENGINE = MergeTree()
ORDER BY tuple();

