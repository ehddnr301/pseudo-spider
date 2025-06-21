-- ClickHouse DDL for database: store_1
-- Generated from: spider_data/database/store_1/store_1.sqlite

CREATE DATABASE IF NOT EXISTS store_1;

CREATE TABLE `store_1`.`artists` (
    `id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`sqlite_sequence` (
    `name` Nullable(String),
    `seq` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `store_1`.`albums` (
    `id` Int64,
    `title` String,
    `artist_id` Int64
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`employees` (
    `id` Int64,
    `last_name` String,
    `first_name` String,
    `title` Nullable(String),
    `reports_to` Nullable(Int64),
    `birth_date` Nullable(DateTime),
    `hire_date` Nullable(DateTime),
    `address` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `country` Nullable(String),
    `postal_code` Nullable(String),
    `phone` Nullable(String),
    `fax` Nullable(String),
    `email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`customers` (
    `id` Int64,
    `first_name` String,
    `last_name` String,
    `company` Nullable(String),
    `address` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `country` Nullable(String),
    `postal_code` Nullable(String),
    `phone` Nullable(String),
    `fax` Nullable(String),
    `email` String,
    `support_rep_id` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`genres` (
    `id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`invoices` (
    `id` Int64,
    `customer_id` Int64,
    `invoice_date` DateTime,
    `billing_address` Nullable(String),
    `billing_city` Nullable(String),
    `billing_state` Nullable(String),
    `billing_country` Nullable(String),
    `billing_postal_code` Nullable(String),
    `total` Decimal64(2)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`media_types` (
    `id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`tracks` (
    `id` Int64,
    `name` String,
    `album_id` Nullable(Int64),
    `media_type_id` Int64,
    `genre_id` Nullable(Int64),
    `composer` Nullable(String),
    `milliseconds` Int64,
    `bytes` Nullable(Int64),
    `unit_price` Decimal64(2)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`invoice_lines` (
    `id` Int64,
    `invoice_id` Int64,
    `track_id` Int64,
    `unit_price` Decimal64(2),
    `quantity` Int64
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`playlists` (
    `id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `store_1`.`playlist_tracks` (
    `playlist_id` Int64,
    `track_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`playlist_id`, `track_id`);

