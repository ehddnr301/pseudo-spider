-- ClickHouse DDL for database: music_2
-- Generated from: spider_data/database/music_2/music_2.sqlite

CREATE DATABASE IF NOT EXISTS music_2;

CREATE TABLE `music_2`.`Songs` (
    `SongId` Int64,
    `Title` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `SongId`;

CREATE TABLE `music_2`.`Albums` (
    `AId` Int64,
    `Title` Nullable(String),
    `Year` Nullable(Int64),
    `Label` Nullable(String),
    `Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `AId`;

CREATE TABLE `music_2`.`Band` (
    `Id` Int64,
    `Firstname` Nullable(String),
    `Lastname` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Id`;

CREATE TABLE `music_2`.`Instruments` (
    `SongId` Int64,
    `BandmateId` Int64,
    `Instrument` String
)
ENGINE = MergeTree()
ORDER BY (`SongId`, `BandmateId`, `Instrument`);

CREATE TABLE `music_2`.`Performance` (
    `SongId` Int64,
    `Bandmate` Int64,
    `StagePosition` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`SongId`, `Bandmate`);

CREATE TABLE `music_2`.`Tracklists` (
    `AlbumId` Int64,
    `Position` Int64,
    `SongId` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`AlbumId`, `Position`);

CREATE TABLE `music_2`.`Vocals` (
    `SongId` Int64,
    `Bandmate` Int64,
    `Type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`SongId`, `Bandmate`);

