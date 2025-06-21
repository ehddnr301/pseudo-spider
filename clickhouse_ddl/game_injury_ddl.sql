-- ClickHouse DDL for database: game_injury
-- Generated from: spider_data/database/game_injury/game_injury.sqlite

CREATE DATABASE IF NOT EXISTS game_injury;

CREATE TABLE `game_injury`.`stadium` (
    `id` Int32,
    `name` Nullable(String),
    `Home_Games` Nullable(Int32),
    `Average_Attendance` Nullable(Float64),
    `Total_Attendance` Nullable(Float64),
    `Capacity_Percentage` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `game_injury`.`game` (
    `stadium_id` Nullable(Int32),
    `id` Int32,
    `Season` Nullable(Int32),
    `Date` Nullable(String),
    `Home_team` Nullable(String),
    `Away_team` Nullable(String),
    `Score` Nullable(String),
    `Competition` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `game_injury`.`injury_accident` (
    `game_id` Nullable(Int32),
    `id` Int32,
    `Player` Nullable(String),
    `Injury` Nullable(String),
    `Number_of_matches` Nullable(String),
    `Source` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

