-- ClickHouse DDL for database: battle_death
-- Generated from: spider_data/database/battle_death/battle_death.sqlite

CREATE DATABASE IF NOT EXISTS battle_death;

CREATE TABLE `battle_death`.`battle` (
    `id` Int32,
    `name` Nullable(String),
    `date` Nullable(String),
    `bulgarian_commander` Nullable(String),
    `latin_commander` Nullable(String),
    `result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `battle_death`.`ship` (
    `lost_in_battle` Nullable(Int32),
    `id` Int32,
    `name` Nullable(String),
    `tonnage` Nullable(String),
    `ship_type` Nullable(String),
    `location` Nullable(String),
    `disposition_of_ship` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `battle_death`.`death` (
    `caused_by_ship_id` Nullable(Int32),
    `id` Int32,
    `note` Nullable(String),
    `killed` Nullable(Int32),
    `injured` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `id`;

