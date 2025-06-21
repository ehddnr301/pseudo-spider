-- ClickHouse DDL for database: document_management
-- Generated from: spider_data/database/document_management/document_management.sqlite

CREATE DATABASE IF NOT EXISTS document_management;

CREATE TABLE `document_management`.`Roles` (
    `role_code` String,
    `role_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `role_code`;

CREATE TABLE `document_management`.`Users` (
    `user_id` Int64,
    `role_code` String,
    `user_name` Nullable(String),
    `user_login` Nullable(String),
    `password` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `user_id`;

CREATE TABLE `document_management`.`Document_Structures` (
    `document_structure_code` String,
    `parent_document_structure_code` Nullable(String),
    `document_structure_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `document_structure_code`;

CREATE TABLE `document_management`.`Functional_Areas` (
    `functional_area_code` String,
    `parent_functional_area_code` Nullable(String),
    `functional_area_description` String
)
ENGINE = MergeTree()
ORDER BY `functional_area_code`;

CREATE TABLE `document_management`.`Images` (
    `image_id` Int64,
    `image_alt_text` Nullable(String),
    `image_name` Nullable(String),
    `image_url` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `image_id`;

CREATE TABLE `document_management`.`Documents` (
    `document_code` String,
    `document_structure_code` String,
    `document_type_code` String,
    `access_count` Nullable(Int64),
    `document_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `document_code`;

CREATE TABLE `document_management`.`Document_Functional_Areas` (
    `document_code` String,
    `functional_area_code` String
)
ENGINE = MergeTree()
ORDER BY (`document_code`, `functional_area_code`);

CREATE TABLE `document_management`.`Document_Sections` (
    `section_id` Int64,
    `document_code` String,
    `section_sequence` Nullable(Int64),
    `section_code` Nullable(String),
    `section_title` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `section_id`;

CREATE TABLE `document_management`.`Document_Sections_Images` (
    `section_id` Int64,
    `image_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`section_id`, `image_id`);

