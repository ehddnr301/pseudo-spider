-- ClickHouse DDL for database: music_1
-- Generated from: spider_data/database/music_1/music_1.sqlite

CREATE DATABASE IF NOT EXISTS music_1;

CREATE TABLE `music_1`.`genre` (
    `g_name` String,
    `rating` Nullable(String),
    `most_popular_in` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `g_name`;

CREATE TABLE `music_1`.`artist` (
    `artist_name` String,
    `country` Nullable(String),
    `gender` Nullable(String),
    `preferred_genre` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `artist_name`;

CREATE TABLE `music_1`.`files` (
    `f_id` String,
    `artist_name` Nullable(String),
    `file_size` Nullable(String),
    `duration` Nullable(String),
    `formats` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `f_id`;

CREATE TABLE `music_1`.`song` (
    `song_name` String,
    `artist_name` Nullable(String),
    `country` Nullable(String),
    `f_id` Nullable(String),
    `genre_is` Nullable(String),
    `rating` Nullable(String),
    `languages` Nullable(String),
    `releasedate` Nullable(Date),
    `resolution` String
)
ENGINE = MergeTree()
ORDER BY `song_name`;

