-- ClickHouse DDL for database: browser_web
-- Generated from: spider_data/database/browser_web/browser_web.sqlite

CREATE DATABASE IF NOT EXISTS browser_web;

CREATE TABLE `browser_web`.`Web_client_accelerator` (
    `id` Int32,
    `name` Nullable(String),
    `Operating_system` Nullable(String),
    `Client` Nullable(String),
    `Connection` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `browser_web`.`browser` (
    `id` Int32,
    `name` Nullable(String),
    `market_share` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `browser_web`.`accelerator_compatible_browser` (
    `accelerator_id` Int32,
    `browser_id` Int32,
    `compatible_since_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`accelerator_id`, `browser_id`);

