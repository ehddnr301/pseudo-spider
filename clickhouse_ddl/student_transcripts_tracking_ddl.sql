-- ClickHouse DDL for database: student_transcripts_tracking
-- Generated from: spider_data/database/student_transcripts_tracking/student_transcripts_tracking.sqlite

CREATE DATABASE IF NOT EXISTS student_transcripts_tracking;

CREATE TABLE `student_transcripts_tracking`.`Addresses` (
    `address_id` Int64,
    `line_1` Nullable(String),
    `line_2` Nullable(String),
    `line_3` Nullable(String),
    `city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String),
    `other_address_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `student_transcripts_tracking`.`Courses` (
    `course_id` Int64,
    `course_name` Nullable(String),
    `course_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `course_id`;

CREATE TABLE `student_transcripts_tracking`.`Departments` (
    `department_id` Int64,
    `department_name` Nullable(String),
    `department_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `department_id`;

CREATE TABLE `student_transcripts_tracking`.`Degree_Programs` (
    `degree_program_id` Int64,
    `department_id` Int64,
    `degree_summary_name` Nullable(String),
    `degree_summary_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `degree_program_id`;

CREATE TABLE `student_transcripts_tracking`.`Sections` (
    `section_id` Int64,
    `course_id` Int64,
    `section_name` Nullable(String),
    `section_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `section_id`;

CREATE TABLE `student_transcripts_tracking`.`Semesters` (
    `semester_id` Int64,
    `semester_name` Nullable(String),
    `semester_description` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `semester_id`;

CREATE TABLE `student_transcripts_tracking`.`Students` (
    `student_id` Int64,
    `current_address_id` Int64,
    `permanent_address_id` Int64,
    `first_name` Nullable(String),
    `middle_name` Nullable(String),
    `last_name` Nullable(String),
    `cell_mobile_number` Nullable(String),
    `email_address` Nullable(String),
    `ssn` Nullable(String),
    `date_first_registered` Nullable(DateTime),
    `date_left` Nullable(DateTime),
    `other_student_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `student_id`;

CREATE TABLE `student_transcripts_tracking`.`Student_Enrolment` (
    `student_enrolment_id` Int64,
    `degree_program_id` Int64,
    `semester_id` Int64,
    `student_id` Int64,
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `student_enrolment_id`;

CREATE TABLE `student_transcripts_tracking`.`Student_Enrolment_Courses` (
    `student_course_id` Int64,
    `course_id` Int64,
    `student_enrolment_id` Int64
)
ENGINE = MergeTree()
ORDER BY `student_course_id`;

CREATE TABLE `student_transcripts_tracking`.`Transcripts` (
    `transcript_id` Int64,
    `transcript_date` Nullable(DateTime),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `transcript_id`;

CREATE TABLE `student_transcripts_tracking`.`Transcript_Contents` (
    `student_course_id` Int64,
    `transcript_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`student_course_id`, `transcript_id`);

