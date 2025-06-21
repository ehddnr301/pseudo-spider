-- ClickHouse DDL for database: world_1
-- Generated from: spider_data/database/world_1/world_1.sqlite

CREATE DATABASE IF NOT EXISTS world_1;

CREATE TABLE `world_1`.`city` (
    `ID` Int64,
    `Name` String DEFAULT '',
    `CountryCode` String DEFAULT '',
    `District` String DEFAULT '',
    `Population` Int64 DEFAULT '0'
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `world_1`.`sqlite_sequence` (
    `name` Nullable(String),
    `seq` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `world_1`.`country` (
    `Code` String DEFAULT '',
    `Name` String DEFAULT '',
    `Continent` String DEFAULT 'Asia',
    `Region` String DEFAULT '',
    `SurfaceArea` Float32 DEFAULT '0.00',
    `IndepYear` Nullable(Int64),
    `Population` Int64 DEFAULT '0',
    `LifeExpectancy` Nullable(Float32),
    `GNP` Nullable(Float32),
    `GNPOld` Nullable(Float32),
    `LocalName` String DEFAULT '',
    `GovernmentForm` String DEFAULT '',
    `HeadOfState` Nullable(String),
    `Capital` Nullable(Int64),
    `Code2` String DEFAULT ''
)
ENGINE = MergeTree()
ORDER BY `Code`;

CREATE TABLE `world_1`.`countrylanguage` (
    `CountryCode` String DEFAULT '',
    `Language` String DEFAULT '',
    `IsOfficial` String DEFAULT 'F',
    `Percentage` Float32 DEFAULT '0.0'
)
ENGINE = MergeTree()
ORDER BY (`CountryCode`, `Language`);

