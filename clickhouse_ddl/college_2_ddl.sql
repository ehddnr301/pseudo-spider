-- ClickHouse DDL for database: college_2
-- Generated from: spider_data/database/college_2/college_2.sqlite

CREATE DATABASE IF NOT EXISTS college_2;

CREATE TABLE `college_2`.`classroom` (
    `building` String,
    `room_number` String,
    `capacity` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY (`building`, `room_number`);

CREATE TABLE `college_2`.`department` (
    `dept_name` String,
    `building` Nullable(String),
    `budget` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `dept_name`;

CREATE TABLE `college_2`.`course` (
    `course_id` String,
    `title` Nullable(String),
    `dept_name` Nullable(String),
    `credits` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `course_id`;

CREATE TABLE `college_2`.`instructor` (
    `ID` String,
    `name` String,
    `dept_name` Nullable(String),
    `salary` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `college_2`.`section` (
    `course_id` String,
    `sec_id` String,
    `semester` String,
    `year` Decimal64(2),
    `building` Nullable(String),
    `room_number` Nullable(String),
    `time_slot_id` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`course_id`, `sec_id`, `semester`, `year`);

CREATE TABLE `college_2`.`teaches` (
    `ID` String,
    `course_id` String,
    `sec_id` String,
    `semester` String,
    `year` Decimal64(2)
)
ENGINE = MergeTree()
ORDER BY (`ID`, `course_id`, `sec_id`, `semester`, `year`);

CREATE TABLE `college_2`.`student` (
    `ID` String,
    `name` String,
    `dept_name` Nullable(String),
    `tot_cred` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `ID`;

CREATE TABLE `college_2`.`takes` (
    `ID` String,
    `course_id` String,
    `sec_id` String,
    `semester` String,
    `year` Decimal64(2),
    `grade` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`ID`, `course_id`, `sec_id`, `semester`, `year`);

CREATE TABLE `college_2`.`advisor` (
    `s_ID` String,
    `i_ID` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `s_ID`;

CREATE TABLE `college_2`.`time_slot` (
    `time_slot_id` String,
    `day` String,
    `start_hr` Decimal64(2),
    `start_min` Decimal64(2),
    `end_hr` Nullable(Decimal64(2)),
    `end_min` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY (`time_slot_id`, `day`, `start_hr`, `start_min`);

CREATE TABLE `college_2`.`prereq` (
    `course_id` String,
    `prereq_id` String
)
ENGINE = MergeTree()
ORDER BY (`course_id`, `prereq_id`);

