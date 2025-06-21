-- ClickHouse DDL for database: yelp
-- Generated from: spider_data/database/yelp/yelp.sqlite

CREATE DATABASE IF NOT EXISTS yelp;

CREATE TABLE `yelp`.`business` (
    `bid` Int32,
    `business_id` Nullable(String),
    `name` Nullable(String),
    `full_address` Nullable(String),
    `city` Nullable(String),
    `latitude` Nullable(String),
    `longitude` Nullable(String),
    `review_count` Nullable(Int32),
    `is_open` Nullable(Int32),
    `rating` Nullable(Float64),
    `state` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `bid`;

CREATE TABLE `yelp`.`category` (
    `id` Int32,
    `business_id` Nullable(String),
    `category_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `yelp`.`user` (
    `uid` Int32,
    `user_id` Nullable(String),
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `uid`;

CREATE TABLE `yelp`.`checkin` (
    `cid` Int32,
    `business_id` Nullable(String),
    `count` Nullable(Int32),
    `day` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `cid`;

CREATE TABLE `yelp`.`neighbourhood` (
    `id` Int32,
    `business_id` Nullable(String),
    `neighbourhood_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `yelp`.`review` (
    `rid` Int32,
    `business_id` Nullable(String),
    `user_id` Nullable(String),
    `rating` Nullable(Float64),
    `text` Nullable(String),
    `year` Nullable(Int32),
    `month` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `rid`;

CREATE TABLE `yelp`.`tip` (
    `tip_id` Int32,
    `business_id` Nullable(String),
    `text` Nullable(String),
    `user_id` Nullable(String),
    `likes` Nullable(Int32),
    `year` Nullable(Int32),
    `month` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `tip_id`;

