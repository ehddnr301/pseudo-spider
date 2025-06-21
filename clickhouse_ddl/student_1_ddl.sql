-- ClickHouse DDL for database: student_1
-- Generated from: spider_data/database/student_1/student_1.sqlite

CREATE DATABASE IF NOT EXISTS student_1;

CREATE TABLE `student_1`.`list` (
    `LastName` String,
    `FirstName` String,
    `Grade` Nullable(Int64),
    `Classroom` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`LastName`, `FirstName`);

CREATE TABLE `student_1`.`teachers` (
    `LastName` String,
    `FirstName` String,
    `Classroom` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`LastName`, `FirstName`);

