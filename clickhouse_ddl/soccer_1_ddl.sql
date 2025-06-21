-- ClickHouse DDL for database: soccer_1
-- Generated from: spider_data/database/soccer_1/soccer_1.sqlite

CREATE DATABASE IF NOT EXISTS soccer_1;

CREATE TABLE `soccer_1`.`Player_Attributes` (
    `id` Int64,
    `player_fifa_api_id` Nullable(Int64),
    `player_api_id` Nullable(Int64),
    `date` Nullable(String),
    `overall_rating` Nullable(Int64),
    `potential` Nullable(Int64),
    `preferred_foot` Nullable(String),
    `attacking_work_rate` Nullable(String),
    `defensive_work_rate` Nullable(String),
    `crossing` Nullable(Int64),
    `finishing` Nullable(Int64),
    `heading_accuracy` Nullable(Int64),
    `short_passing` Nullable(Int64),
    `volleys` Nullable(Int64),
    `dribbling` Nullable(Int64),
    `curve` Nullable(Int64),
    `free_kick_accuracy` Nullable(Int64),
    `long_passing` Nullable(Int64),
    `ball_control` Nullable(Int64),
    `acceleration` Nullable(Int64),
    `sprint_speed` Nullable(Int64),
    `agility` Nullable(Int64),
    `reactions` Nullable(Int64),
    `balance` Nullable(Int64),
    `shot_power` Nullable(Int64),
    `jumping` Nullable(Int64),
    `stamina` Nullable(Int64),
    `strength` Nullable(Int64),
    `long_shots` Nullable(Int64),
    `aggression` Nullable(Int64),
    `interceptions` Nullable(Int64),
    `positioning` Nullable(Int64),
    `vision` Nullable(Int64),
    `penalties` Nullable(Int64),
    `marking` Nullable(Int64),
    `standing_tackle` Nullable(Int64),
    `sliding_tackle` Nullable(Int64),
    `gk_diving` Nullable(Int64),
    `gk_handling` Nullable(Int64),
    `gk_kicking` Nullable(Int64),
    `gk_positioning` Nullable(Int64),
    `gk_reflexes` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `soccer_1`.`sqlite_sequence` (
    `name` Nullable(String),
    `seq` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `soccer_1`.`Player` (
    `id` Int64,
    `player_api_id` Nullable(Int64),
    `player_name` Nullable(String),
    `player_fifa_api_id` Nullable(Int64),
    `birthday` Nullable(String),
    `height` Nullable(Int64),
    `weight` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `soccer_1`.`League` (
    `id` Int64,
    `country_id` Nullable(Int64),
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `soccer_1`.`Country` (
    `id` Int64,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `soccer_1`.`Team` (
    `id` Int64,
    `team_api_id` Nullable(Int64),
    `team_fifa_api_id` Nullable(Int64),
    `team_long_name` Nullable(String),
    `team_short_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `soccer_1`.`Team_Attributes` (
    `id` Int64,
    `team_fifa_api_id` Nullable(Int64),
    `team_api_id` Nullable(Int64),
    `date` Nullable(String),
    `buildUpPlaySpeed` Nullable(Int64),
    `buildUpPlaySpeedClass` Nullable(String),
    `buildUpPlayDribbling` Nullable(Int64),
    `buildUpPlayDribblingClass` Nullable(String),
    `buildUpPlayPassing` Nullable(Int64),
    `buildUpPlayPassingClass` Nullable(String),
    `buildUpPlayPositioningClass` Nullable(String),
    `chanceCreationPassing` Nullable(Int64),
    `chanceCreationPassingClass` Nullable(String),
    `chanceCreationCrossing` Nullable(Int64),
    `chanceCreationCrossingClass` Nullable(String),
    `chanceCreationShooting` Nullable(Int64),
    `chanceCreationShootingClass` Nullable(String),
    `chanceCreationPositioningClass` Nullable(String),
    `defencePressure` Nullable(Int64),
    `defencePressureClass` Nullable(String),
    `defenceAggression` Nullable(Int64),
    `defenceAggressionClass` Nullable(String),
    `defenceTeamWidth` Nullable(Int64),
    `defenceTeamWidthClass` Nullable(String),
    `defenceDefenderLineClass` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

