-- ClickHouse DDL for database: network_2
-- Generated from: spider_data/database/network_2/network_2.sqlite

CREATE DATABASE IF NOT EXISTS network_2;

CREATE TABLE `network_2`.`Person` (
    `name` String,
    `age` Nullable(Int64),
    `city` Nullable(String),
    `gender` Nullable(String),
    `job` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `name`;

CREATE TABLE `network_2`.`PersonFriend` (
    `name` Nullable(String),
    `friend` Nullable(String),
    `year` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY tuple();

