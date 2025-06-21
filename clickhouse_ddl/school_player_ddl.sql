-- ClickHouse DDL for database: school_player
-- Generated from: spider_data/database/school_player/school_player.sqlite

CREATE DATABASE IF NOT EXISTS school_player;

CREATE TABLE `school_player`.`school` (
    `School_ID` Int32,
    `School` Nullable(String),
    `Location` Nullable(String),
    `Enrollment` Nullable(Float64),
    `Founded` Nullable(Float64),
    `Denomination` Nullable(String),
    `Boys_or_Girls` Nullable(String),
    `Day_or_Boarding` Nullable(String),
    `Year_Entered_Competition` Nullable(Float64),
    `School_Colors` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `School_ID`;

CREATE TABLE `school_player`.`school_details` (
    `School_ID` Int32,
    `Nickname` Nullable(String),
    `Colors` Nullable(String),
    `League` Nullable(String),
    `Class` Nullable(String),
    `Division` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `School_ID`;

CREATE TABLE `school_player`.`school_performance` (
    `School_Id` Int32,
    `School_Year` String,
    `Class_A` Nullable(String),
    `Class_AA` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`School_Id`, `School_Year`);

CREATE TABLE `school_player`.`player` (
    `Player_ID` Int32,
    `Player` Nullable(String),
    `Team` Nullable(String),
    `Age` Nullable(Int32),
    `Position` Nullable(String),
    `School_ID` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Player_ID`;

