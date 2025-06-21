-- ClickHouse DDL for database: poker_player
-- Generated from: spider_data/database/poker_player/poker_player.sqlite

CREATE DATABASE IF NOT EXISTS poker_player;

CREATE TABLE `poker_player`.`poker_player` (
    `Poker_Player_ID` Int32,
    `People_ID` Nullable(Int32),
    `Final_Table_Made` Nullable(Float64),
    `Best_Finish` Nullable(Float64),
    `Money_Rank` Nullable(Float64),
    `Earnings` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `Poker_Player_ID`;

CREATE TABLE `poker_player`.`people` (
    `People_ID` Int32,
    `Nationality` Nullable(String),
    `Name` Nullable(String),
    `Birth_Date` Nullable(String),
    `Height` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY `People_ID`;

