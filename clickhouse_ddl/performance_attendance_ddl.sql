-- ClickHouse DDL for database: performance_attendance
-- Generated from: spider_data/database/performance_attendance/performance_attendance.sqlite

CREATE DATABASE IF NOT EXISTS performance_attendance;

CREATE TABLE `performance_attendance`.`member` (
    `Member_ID` String,
    `Name` Nullable(String),
    `Nationality` Nullable(String),
    `Role` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `performance_attendance`.`performance` (
    `Performance_ID` Float64,
    `Date` Nullable(String),
    `Host` Nullable(String),
    `Location` Nullable(String),
    `Attendance` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Performance_ID`;

CREATE TABLE `performance_attendance`.`member_attendance` (
    `Member_ID` Int32,
    `Performance_ID` Int32,
    `Num_of_Pieces` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`Member_ID`, `Performance_ID`);

