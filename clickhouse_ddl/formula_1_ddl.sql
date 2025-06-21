-- ClickHouse DDL for database: formula_1
-- Generated from: spider_data/database/formula_1/formula_1.sqlite

CREATE DATABASE IF NOT EXISTS formula_1;

CREATE TABLE `formula_1`.`circuits` (
    `circuitId` Int64,
    `circuitRef` Nullable(String),
    `name` Nullable(String),
    `location` Nullable(String),
    `country` Nullable(String),
    `lat` Nullable(Float64),
    `lng` Nullable(Float64),
    `alt` Nullable(String),
    `url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `circuitId`;

CREATE TABLE `formula_1`.`races` (
    `raceId` Int64,
    `year` Nullable(Int64),
    `round` Nullable(Int64),
    `circuitId` Nullable(Int64),
    `name` Nullable(String),
    `date` Nullable(String),
    `time` Nullable(String),
    `url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `raceId`;

CREATE TABLE `formula_1`.`drivers` (
    `driverId` Int64,
    `driverRef` Nullable(String),
    `number` Nullable(String),
    `code` Nullable(String),
    `forename` Nullable(String),
    `surname` Nullable(String),
    `dob` Nullable(String),
    `nationality` Nullable(String),
    `url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `driverId`;

CREATE TABLE `formula_1`.`status` (
    `statusId` Int64,
    `status` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `statusId`;

CREATE TABLE `formula_1`.`seasons` (
    `year` Int64,
    `url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `year`;

CREATE TABLE `formula_1`.`constructors` (
    `constructorId` Int64,
    `constructorRef` Nullable(String),
    `name` Nullable(String),
    `nationality` Nullable(String),
    `url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `constructorId`;

CREATE TABLE `formula_1`.`constructorStandings` (
    `constructorStandingsId` Int64,
    `raceId` Nullable(Int64),
    `constructorId` Nullable(Int64),
    `points` Nullable(Float64),
    `position` Nullable(Int64),
    `positionText` Nullable(String),
    `wins` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `constructorStandingsId`;

CREATE TABLE `formula_1`.`results` (
    `resultId` Int64,
    `raceId` Nullable(Int64),
    `driverId` Nullable(Int64),
    `constructorId` Nullable(Int64),
    `number` Nullable(Int64),
    `grid` Nullable(Int64),
    `position` Nullable(String),
    `positionText` Nullable(String),
    `positionOrder` Nullable(Int64),
    `points` Nullable(Float64),
    `laps` Nullable(String),
    `time` Nullable(String),
    `milliseconds` Nullable(String),
    `fastestLap` Nullable(String),
    `rank` Nullable(String),
    `fastestLapTime` Nullable(String),
    `fastestLapSpeed` Nullable(String),
    `statusId` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `resultId`;

CREATE TABLE `formula_1`.`driverStandings` (
    `driverStandingsId` Int64,
    `raceId` Nullable(Int64),
    `driverId` Nullable(Int64),
    `points` Nullable(Float64),
    `position` Nullable(Int64),
    `positionText` Nullable(String),
    `wins` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `driverStandingsId`;

CREATE TABLE `formula_1`.`constructorResults` (
    `constructorResultsId` Int64,
    `raceId` Nullable(Int64),
    `constructorId` Nullable(Int64),
    `points` Nullable(Float64),
    `status` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `constructorResultsId`;

CREATE TABLE `formula_1`.`qualifying` (
    `qualifyId` Int64,
    `raceId` Nullable(Int64),
    `driverId` Nullable(Int64),
    `constructorId` Nullable(Int64),
    `number` Nullable(Int64),
    `position` Nullable(Int64),
    `q1` Nullable(String),
    `q2` Nullable(String),
    `q3` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `qualifyId`;

CREATE TABLE `formula_1`.`pitStops` (
    `raceId` Int64,
    `driverId` Int64,
    `stop` Int64,
    `lap` Nullable(Int64),
    `time` Nullable(String),
    `duration` Nullable(String),
    `milliseconds` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`raceId`, `driverId`, `stop`);

CREATE TABLE `formula_1`.`lapTimes` (
    `raceId` Int64,
    `driverId` Int64,
    `lap` Int64,
    `position` Nullable(Int64),
    `time` Nullable(String),
    `milliseconds` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`raceId`, `driverId`, `lap`);

