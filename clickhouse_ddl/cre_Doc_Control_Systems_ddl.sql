-- ClickHouse DDL for database: cre_Doc_Control_Systems
-- Generated from: spider_data/database/cre_Doc_Control_Systems/cre_Doc_Control_Systems.sqlite

CREATE DATABASE IF NOT EXISTS cre_Doc_Control_Systems;

CREATE TABLE `cre_Doc_Control_Systems`.`Ref_Document_Types` (
    `document_type_code` String,
    `document_type_description` String
)
ENGINE = MergeTree()
ORDER BY `document_type_code`;

CREATE TABLE `cre_Doc_Control_Systems`.`Roles` (
    `role_code` String,
    `role_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `role_code`;

CREATE TABLE `cre_Doc_Control_Systems`.`Addresses` (
    `address_id` Int64,
    `address_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `cre_Doc_Control_Systems`.`Ref_Document_Status` (
    `document_status_code` String,
    `document_status_description` String
)
ENGINE = MergeTree()
ORDER BY `document_status_code`;

CREATE TABLE `cre_Doc_Control_Systems`.`Ref_Shipping_Agents` (
    `shipping_agent_code` String,
    `shipping_agent_name` String,
    `shipping_agent_description` String
)
ENGINE = MergeTree()
ORDER BY `shipping_agent_code`;

CREATE TABLE `cre_Doc_Control_Systems`.`Documents` (
    `document_id` Int64,
    `document_status_code` String,
    `document_type_code` String,
    `shipping_agent_code` Nullable(String),
    `receipt_date` Nullable(DateTime),
    `receipt_number` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `document_id`;

CREATE TABLE `cre_Doc_Control_Systems`.`Employees` (
    `employee_id` Int64,
    `role_code` String,
    `employee_name` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `employee_id`;

CREATE TABLE `cre_Doc_Control_Systems`.`Document_Drafts` (
    `document_id` Int64,
    `draft_number` Int64,
    `draft_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`document_id`, `draft_number`);

CREATE TABLE `cre_Doc_Control_Systems`.`Draft_Copies` (
    `document_id` Int64,
    `draft_number` Int64,
    `copy_number` Int64
)
ENGINE = MergeTree()
ORDER BY (`document_id`, `draft_number`, `copy_number`);

CREATE TABLE `cre_Doc_Control_Systems`.`Circulation_History` (
    `document_id` Int64,
    `draft_number` Int64,
    `copy_number` Int64,
    `employee_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`document_id`, `draft_number`, `copy_number`, `employee_id`);

CREATE TABLE `cre_Doc_Control_Systems`.`Documents_Mailed` (
    `document_id` Int64,
    `mailed_to_address_id` Int64,
    `mailing_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`document_id`, `mailed_to_address_id`);

