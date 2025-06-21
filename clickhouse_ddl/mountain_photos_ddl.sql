-- ClickHouse DDL for database: mountain_photos
-- Generated from: spider_data/database/mountain_photos/mountain_photos.sqlite

CREATE DATABASE IF NOT EXISTS mountain_photos;

CREATE TABLE `mountain_photos`.`mountain` (
    `id` Int32,
    `name` Nullable(String),
    `Height` Nullable(Float64),
    `Prominence` Nullable(Float64),
    `Range` Nullable(String),
    `Country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `mountain_photos`.`camera_lens` (
    `id` Int32,
    `brand` Nullable(String),
    `name` Nullable(String),
    `focal_length_mm` Nullable(Float64),
    `max_aperture` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `mountain_photos`.`photos` (
    `id` Int32,
    `camera_lens_id` Nullable(Int32),
    `mountain_id` Nullable(Int32),
    `color` Nullable(String),
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

