-- ClickHouse DDL for database: architecture
-- Generated from: spider_data/database/architecture/architecture.sqlite

CREATE DATABASE IF NOT EXISTS architecture;

CREATE TABLE `architecture`.`architect` (
    `id` String,
    `name` Nullable(String),
    `nationality` Nullable(String),
    `gender` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `architecture`.`bridge` (
    `architect_id` Nullable(Int32),
    `id` Int32,
    `name` Nullable(String),
    `location` Nullable(String),
    `length_meters` Nullable(Float64),
    `length_feet` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `architecture`.`mill` (
    `architect_id` Nullable(Int32),
    `id` Int32,
    `location` Nullable(String),
    `name` Nullable(String),
    `type` Nullable(String),
    `built_year` Nullable(Int32),
    `notes` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

