-- ClickHouse DDL for database: voter_1
-- Generated from: spider_data/database/voter_1/voter_1.sqlite

CREATE DATABASE IF NOT EXISTS voter_1;

CREATE TABLE `voter_1`.`AREA_CODE_STATE` (
    `area_code` Int64,
    `state` String
)
ENGINE = MergeTree()
ORDER BY `area_code`;

CREATE TABLE `voter_1`.`CONTESTANTS` (
    `contestant_number` Int64,
    `contestant_name` String
)
ENGINE = MergeTree()
ORDER BY `contestant_number`;

CREATE TABLE `voter_1`.`VOTES` (
    `vote_id` Int64,
    `phone_number` Int64,
    `state` String,
    `contestant_number` Int64,
    `created` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `vote_id`;

