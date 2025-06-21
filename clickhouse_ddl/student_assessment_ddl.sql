-- ClickHouse DDL for database: student_assessment
-- Generated from: spider_data/database/student_assessment/student_assessment.sqlite

CREATE DATABASE IF NOT EXISTS student_assessment;

CREATE TABLE `student_assessment`.`Addresses` (
    `address_id` Int64,
    `line_1` Nullable(String),
    `line_2` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `student_assessment`.`People` (
    `person_id` Int64,
    `first_name` Nullable(String),
    `middle_name` Nullable(String),
    `last_name` Nullable(String),
    `cell_mobile_number` Nullable(String),
    `email_address` Nullable(String),
    `login_name` Nullable(String),
    `password` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `person_id`;

CREATE TABLE `student_assessment`.`Students` (
    `student_id` Int64,
    `student_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `student_id`;

CREATE TABLE `student_assessment`.`Courses` (
    `course_id` String,
    `course_name` Nullable(String),
    `course_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `course_id`;

CREATE TABLE `student_assessment`.`People_Addresses` (
    `person_address_id` Int64,
    `person_id` Int64,
    `address_id` Int64,
    `date_from` Nullable(DateTime),
    `date_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `person_address_id`;

CREATE TABLE `student_assessment`.`Student_Course_Registrations` (
    `student_id` Int64,
    `course_id` Int64,
    `registration_date` DateTime
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `course_id`);

CREATE TABLE `student_assessment`.`Student_Course_Attendance` (
    `student_id` Int64,
    `course_id` Int64,
    `date_of_attendance` DateTime
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `course_id`);

CREATE TABLE `student_assessment`.`Candidates` (
    `candidate_id` Int64,
    `candidate_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `candidate_id`;

CREATE TABLE `student_assessment`.`Candidate_Assessments` (
    `candidate_id` Int64,
    `qualification` String,
    `assessment_date` DateTime,
    `asessment_outcome_code` String
)
ENGINE = MergeTree()
ORDER BY (`candidate_id`, `qualification`);

