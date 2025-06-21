-- ClickHouse DDL for database: course_teach
-- Generated from: spider_data/database/course_teach/course_teach.sqlite

CREATE DATABASE IF NOT EXISTS course_teach;

CREATE TABLE `course_teach`.`course` (
    `Course_ID` Int32,
    `Staring_Date` Nullable(String),
    `Course` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Course_ID`;

CREATE TABLE `course_teach`.`teacher` (
    `Teacher_ID` Int32,
    `Name` Nullable(String),
    `Age` Nullable(String),
    `Hometown` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Teacher_ID`;

CREATE TABLE `course_teach`.`course_arrange` (
    `Course_ID` Int32,
    `Teacher_ID` Int32,
    `Grade` Int32
)
ENGINE = MergeTree()
ORDER BY (`Course_ID`, `Teacher_ID`, `Grade`);

