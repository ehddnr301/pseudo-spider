-- ClickHouse DDL for database: wta_1
-- Generated from: spider_data/database/wta_1/wta_1.sqlite

CREATE DATABASE IF NOT EXISTS wta_1;

CREATE TABLE `wta_1`.`players` (
    `player_id` Int32,
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `hand` Nullable(String),
    `birth_date` Nullable(Date),
    `country_code` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `player_id`;

CREATE TABLE `wta_1`.`matches` (
    `best_of` Nullable(Int32),
    `draw_size` Nullable(Int32),
    `loser_age` Nullable(Float32),
    `loser_entry` Nullable(String),
    `loser_hand` Nullable(String),
    `loser_ht` Nullable(Int32),
    `loser_id` Nullable(Int32),
    `loser_ioc` Nullable(String),
    `loser_name` Nullable(String),
    `loser_rank` Nullable(Int32),
    `loser_rank_points` Nullable(Int32),
    `loser_seed` Nullable(Int32),
    `match_num` Nullable(Int32),
    `minutes` Nullable(Int32),
    `round` Nullable(String),
    `score` Nullable(String),
    `surface` Nullable(String),
    `tourney_date` Nullable(Date),
    `tourney_id` Nullable(String),
    `tourney_level` Nullable(String),
    `tourney_name` Nullable(String),
    `winner_age` Nullable(Float32),
    `winner_entry` Nullable(String),
    `winner_hand` Nullable(String),
    `winner_ht` Nullable(Int32),
    `winner_id` Nullable(Int32),
    `winner_ioc` Nullable(String),
    `winner_name` Nullable(String),
    `winner_rank` Nullable(Int32),
    `winner_rank_points` Nullable(Int32),
    `winner_seed` Nullable(Int32),
    `year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `wta_1`.`rankings` (
    `ranking_date` Nullable(Date),
    `ranking` Nullable(Int32),
    `player_id` Nullable(Int32),
    `ranking_points` Nullable(Int32),
    `tours` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY tuple();

