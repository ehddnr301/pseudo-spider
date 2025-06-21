-- ClickHouse DDL for database: tvshow
-- Generated from: spider_data/database/tvshow/tvshow.sqlite

CREATE DATABASE IF NOT EXISTS tvshow;

CREATE TABLE `tvshow`.`TV_Channel` (
    `id` String,
    `series_name` Nullable(String),
    `Country` Nullable(String),
    `Language` Nullable(String),
    `Content` Nullable(String),
    `Pixel_aspect_ratio_PAR` Nullable(String),
    `Hight_definition_TV` Nullable(String),
    `Pay_per_view_PPV` Nullable(String),
    `Package_Option` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `tvshow`.`TV_series` (
    `id` Float64,
    `Episode` Nullable(String),
    `Air_Date` Nullable(String),
    `Rating` Nullable(String),
    `Share` Nullable(Float64),
    `18_49_Rating_Share` Nullable(String),
    `Viewers_m` Nullable(String),
    `Weekly_Rank` Nullable(Float64),
    `Channel` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `tvshow`.`Cartoon` (
    `id` Float64,
    `Title` Nullable(String),
    `Directed_by` Nullable(String),
    `Written_by` Nullable(String),
    `Original_air_date` Nullable(String),
    `Production_code` Nullable(Float64),
    `Channel` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

