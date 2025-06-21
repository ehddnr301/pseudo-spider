-- ClickHouse DDL for database: network_1
-- Generated from: spider_data/database/network_1/network_1.sqlite

CREATE DATABASE IF NOT EXISTS network_1;

CREATE TABLE `network_1`.`Highschooler` (
    `ID` Int32,
    `name` Nullable(String),
    `grade` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `network_1`.`Friend` (
    `student_id` Int32,
    `friend_id` Int32
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `friend_id`);

CREATE TABLE `network_1`.`Likes` (
    `student_id` Int32,
    `liked_id` Int32
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `liked_id`);

