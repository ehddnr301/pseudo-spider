-- ClickHouse DDL for database: epinions_1
-- Generated from: spider_data/database/epinions_1/epinions_1.sqlite

CREATE DATABASE IF NOT EXISTS epinions_1;

CREATE TABLE `epinions_1`.`item` (
    `i_id` Int64,
    `title` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `i_id`;

CREATE TABLE `epinions_1`.`review` (
    `a_id` Int64,
    `u_id` Int64,
    `i_id` Int64,
    `rating` Nullable(Int64),
    `rank` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `a_id`;

CREATE TABLE `epinions_1`.`useracct` (
    `u_id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `u_id`;

CREATE TABLE `epinions_1`.`trust` (
    `source_u_id` Int64,
    `target_u_id` Int64,
    `trust` Int64
)
ENGINE = MergeTree()
ORDER BY (`source_u_id`, `target_u_id`, `trust`);

