-- ClickHouse DDL for database: behavior_monitoring
-- Generated from: spider_data/database/behavior_monitoring/behavior_monitoring.sqlite

CREATE DATABASE IF NOT EXISTS behavior_monitoring;

CREATE TABLE `behavior_monitoring`.`Ref_Address_Types` (
    `address_type_code` String,
    `address_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_type_code`;

CREATE TABLE `behavior_monitoring`.`Ref_Detention_Type` (
    `detention_type_code` String,
    `detention_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `detention_type_code`;

CREATE TABLE `behavior_monitoring`.`Ref_Incident_Type` (
    `incident_type_code` String,
    `incident_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `incident_type_code`;

CREATE TABLE `behavior_monitoring`.`Addresses` (
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

CREATE TABLE `behavior_monitoring`.`Students` (
    `student_id` Int64,
    `address_id` Int64,
    `first_name` Nullable(String),
    `middle_name` Nullable(String),
    `last_name` Nullable(String),
    `cell_mobile_number` Nullable(String),
    `email_address` Nullable(String),
    `date_first_rental` Nullable(DateTime),
    `date_left_university` Nullable(DateTime),
    `other_student_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `student_id`;

CREATE TABLE `behavior_monitoring`.`Teachers` (
    `teacher_id` Int64,
    `address_id` Int64,
    `first_name` Nullable(String),
    `middle_name` Nullable(String),
    `last_name` Nullable(String),
    `gender` Nullable(String),
    `cell_mobile_number` Nullable(String),
    `email_address` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `teacher_id`;

CREATE TABLE `behavior_monitoring`.`Assessment_Notes` (
    `notes_id` Int64,
    `student_id` Nullable(Int64),
    `teacher_id` Int64,
    `date_of_notes` Nullable(DateTime),
    `text_of_notes` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`notes_id`, `teacher_id`);

CREATE TABLE `behavior_monitoring`.`Behavior_Incident` (
    `incident_id` Int64,
    `incident_type_code` String,
    `student_id` Int64,
    `date_incident_start` Nullable(DateTime),
    `date_incident_end` Nullable(DateTime),
    `incident_summary` Nullable(String),
    `recommendations` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `incident_id`;

CREATE TABLE `behavior_monitoring`.`Detention` (
    `detention_id` Int64,
    `detention_type_code` String,
    `teacher_id` Nullable(Int64),
    `datetime_detention_start` Nullable(DateTime),
    `datetime_detention_end` Nullable(DateTime),
    `detention_summary` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `detention_id`;

CREATE TABLE `behavior_monitoring`.`Student_Addresses` (
    `student_id` Int64,
    `address_id` Int64,
    `date_address_from` DateTime,
    `date_address_to` Nullable(DateTime),
    `monthly_rental` Nullable(Decimal64(2)),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `address_id`, `date_address_from`);

CREATE TABLE `behavior_monitoring`.`Students_in_Detention` (
    `student_id` Int64,
    `detention_id` Int64,
    `incident_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`student_id`, `detention_id`, `incident_id`);

