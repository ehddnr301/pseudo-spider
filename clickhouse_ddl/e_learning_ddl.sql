-- ClickHouse DDL for database: e_learning
-- Generated from: spider_data/database/e_learning/e_learning.sqlite

CREATE DATABASE IF NOT EXISTS e_learning;

CREATE TABLE `e_learning`.`Course_Authors_and_Tutors` (
    `author_id` Int64,
    `author_tutor_ATB` Nullable(String),
    `login_name` Nullable(String),
    `password` Nullable(String),
    `personal_name` Nullable(String),
    `middle_name` Nullable(String),
    `family_name` Nullable(String),
    `gender_mf` Nullable(String),
    `address_line_1` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `author_id`;

CREATE TABLE `e_learning`.`Students` (
    `student_id` Int64,
    `date_of_registration` Nullable(DateTime),
    `date_of_latest_logon` Nullable(DateTime),
    `login_name` Nullable(String),
    `password` Nullable(String),
    `personal_name` Nullable(String),
    `middle_name` Nullable(String),
    `family_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `student_id`;

CREATE TABLE `e_learning`.`Subjects` (
    `subject_id` Int64,
    `subject_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `subject_id`;

CREATE TABLE `e_learning`.`Courses` (
    `course_id` Int64,
    `author_id` Int64,
    `subject_id` Int64,
    `course_name` Nullable(String),
    `course_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `course_id`;

CREATE TABLE `e_learning`.`Student_Course_Enrolment` (
    `registration_id` Int64,
    `student_id` Int64,
    `course_id` Int64,
    `date_of_enrolment` DateTime,
    `date_of_completion` DateTime
)
ENGINE = MergeTree()
ORDER BY `registration_id`;

CREATE TABLE `e_learning`.`Student_Tests_Taken` (
    `registration_id` Int64,
    `date_test_taken` DateTime,
    `test_result` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`registration_id`, `date_test_taken`);

