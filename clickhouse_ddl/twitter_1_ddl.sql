-- ClickHouse DDL for database: twitter_1
-- Generated from: spider_data/database/twitter_1/twitter_1.sqlite

CREATE DATABASE IF NOT EXISTS twitter_1;

CREATE TABLE `twitter_1`.`follows` (
    `f1` Int32,
    `f2` Int32
)
ENGINE = MergeTree()
ORDER BY (`f1`, `f2`);

CREATE TABLE `twitter_1`.`tweets` (
    `id` Int64,
    `uid` Int32,
    `text` String,
    `createdate` Nullable(DateTime) DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `twitter_1`.`user_profiles` (
    `uid` Int32,
    `name` Nullable(String),
    `email` Nullable(String),
    `partitionid` Nullable(Int32),
    `followers` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `uid`;

