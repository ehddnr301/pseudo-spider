-- ClickHouse DDL for database: tracking_grants_for_research
-- Generated from: spider_data/database/tracking_grants_for_research/tracking_grants_for_research.sqlite

CREATE DATABASE IF NOT EXISTS tracking_grants_for_research;

CREATE TABLE `tracking_grants_for_research`.`Document_Types` (
    `document_type_code` String,
    `document_description` String
)
ENGINE = MergeTree()
ORDER BY `document_type_code`;

CREATE TABLE `tracking_grants_for_research`.`Documents` (
    `document_id` Int64,
    `document_type_code` Nullable(String),
    `grant_id` Int64,
    `sent_date` DateTime,
    `response_received_date` DateTime,
    `other_details` String
)
ENGINE = MergeTree()
ORDER BY `document_id`;

CREATE TABLE `tracking_grants_for_research`.`Grants` (
    `grant_id` Int64,
    `organisation_id` Int64,
    `grant_amount` Decimal64(2) DEFAULT 0,
    `grant_start_date` DateTime,
    `grant_end_date` DateTime,
    `other_details` String
)
ENGINE = MergeTree()
ORDER BY `grant_id`;

CREATE TABLE `tracking_grants_for_research`.`Organisation_Types` (
    `organisation_type` String,
    `organisation_type_description` String
)
ENGINE = MergeTree()
ORDER BY `organisation_type`;

CREATE TABLE `tracking_grants_for_research`.`Organisations` (
    `organisation_id` Int64,
    `organisation_type` String,
    `organisation_details` String
)
ENGINE = MergeTree()
ORDER BY `organisation_id`;

CREATE TABLE `tracking_grants_for_research`.`Project_Outcomes` (
    `project_id` Int64,
    `outcome_code` String,
    `outcome_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`project_id`, `outcome_code`);

CREATE TABLE `tracking_grants_for_research`.`Project_Staff` (
    `staff_id` Float64,
    `project_id` Int64,
    `role_code` String,
    `date_from` Nullable(DateTime),
    `date_to` Nullable(DateTime),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `tracking_grants_for_research`.`Projects` (
    `project_id` Int64,
    `organisation_id` Int64,
    `project_details` String
)
ENGINE = MergeTree()
ORDER BY `project_id`;

CREATE TABLE `tracking_grants_for_research`.`Research_Outcomes` (
    `outcome_code` String,
    `outcome_description` String
)
ENGINE = MergeTree()
ORDER BY `outcome_code`;

CREATE TABLE `tracking_grants_for_research`.`Research_Staff` (
    `staff_id` Int64,
    `employer_organisation_id` Int64,
    `staff_details` String
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `tracking_grants_for_research`.`Staff_Roles` (
    `role_code` String,
    `role_description` String
)
ENGINE = MergeTree()
ORDER BY `role_code`;

CREATE TABLE `tracking_grants_for_research`.`Tasks` (
    `task_id` Int64,
    `project_id` Int64,
    `task_details` String,
    `eg Agree Objectives` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `task_id`;

