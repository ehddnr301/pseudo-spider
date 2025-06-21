-- ClickHouse DDL for database: imdb
-- Generated from: spider_data/database/imdb/imdb.sqlite

CREATE DATABASE IF NOT EXISTS imdb;

CREATE TABLE `imdb`.`actor` (
    `aid` Int32,
    `gender` Nullable(String),
    `name` Nullable(String),
    `nationality` Nullable(String),
    `birth_city` Nullable(String),
    `birth_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `aid`;

CREATE TABLE `imdb`.`copyright` (
    `id` Int32,
    `msid` Nullable(Int32),
    `cid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`cast` (
    `id` Int32,
    `msid` Nullable(Int32),
    `aid` Nullable(Int32),
    `role` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`genre` (
    `gid` Int32,
    `genre` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `gid`;

CREATE TABLE `imdb`.`classification` (
    `id` Int32,
    `msid` Nullable(Int32),
    `gid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`company` (
    `id` Int32,
    `name` Nullable(String),
    `country_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`director` (
    `did` Int32,
    `gender` Nullable(String),
    `name` Nullable(String),
    `nationality` Nullable(String),
    `birth_city` Nullable(String),
    `birth_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `did`;

CREATE TABLE `imdb`.`producer` (
    `pid` Int32,
    `gender` Nullable(String),
    `name` Nullable(String),
    `nationality` Nullable(String),
    `birth_city` Nullable(String),
    `birth_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `pid`;

CREATE TABLE `imdb`.`directed_by` (
    `id` Int32,
    `msid` Nullable(Int32),
    `did` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`keyword` (
    `id` Int32,
    `keyword` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`made_by` (
    `id` Int32,
    `msid` Nullable(Int32),
    `pid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`movie` (
    `mid` Int32,
    `title` Nullable(String),
    `release_year` Nullable(Int32),
    `title_aka` Nullable(String),
    `budget` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `mid`;

CREATE TABLE `imdb`.`tags` (
    `id` Int32,
    `msid` Nullable(Int32),
    `kid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `imdb`.`tv_series` (
    `sid` Int32,
    `title` Nullable(String),
    `release_year` Nullable(Int32),
    `num_of_seasons` Nullable(Int32),
    `num_of_episodes` Nullable(Int32),
    `title_aka` Nullable(String),
    `budget` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `sid`;

CREATE TABLE `imdb`.`writer` (
    `wid` Int32,
    `gender` Nullable(String),
    `name` Nullable(Int32),
    `nationality` Nullable(Int32),
    `num_of_episodes` Nullable(Int32),
    `birth_city` Nullable(String),
    `birth_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `wid`;

CREATE TABLE `imdb`.`written_by` (
    `id` Nullable(Int32),
    `msid` Nullable(Int32),
    `wid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY tuple();

