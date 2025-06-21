-- ClickHouse DDL for database: assets_maintenance
-- Generated from: spider_data/database/assets_maintenance/assets_maintenance.sqlite

CREATE DATABASE IF NOT EXISTS assets_maintenance;

CREATE TABLE `assets_maintenance`.`Third_Party_Companies` (
    `company_id` Int64,
    `company_type` String,
    `company_name` Nullable(String),
    `company_address` Nullable(String),
    `other_company_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `company_id`;

CREATE TABLE `assets_maintenance`.`Maintenance_Contracts` (
    `maintenance_contract_id` Int64,
    `maintenance_contract_company_id` Int64,
    `contract_start_date` Nullable(DateTime),
    `contract_end_date` Nullable(DateTime),
    `other_contract_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `maintenance_contract_id`;

CREATE TABLE `assets_maintenance`.`Parts` (
    `part_id` Int64,
    `part_name` Nullable(String),
    `chargeable_yn` Nullable(String),
    `chargeable_amount` Nullable(String),
    `other_part_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `part_id`;

CREATE TABLE `assets_maintenance`.`Skills` (
    `skill_id` Int64,
    `skill_code` Nullable(String),
    `skill_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `skill_id`;

CREATE TABLE `assets_maintenance`.`Staff` (
    `staff_id` Int64,
    `staff_name` Nullable(String),
    `gender` Nullable(String),
    `other_staff_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `assets_maintenance`.`Assets` (
    `asset_id` Int64,
    `maintenance_contract_id` Int64,
    `supplier_company_id` Int64,
    `asset_details` Nullable(String),
    `asset_make` Nullable(String),
    `asset_model` Nullable(String),
    `asset_acquired_date` Nullable(DateTime),
    `asset_disposed_date` Nullable(DateTime),
    `other_asset_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `asset_id`;

CREATE TABLE `assets_maintenance`.`Asset_Parts` (
    `asset_id` Int64,
    `part_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`asset_id`, `part_id`);

CREATE TABLE `assets_maintenance`.`Maintenance_Engineers` (
    `engineer_id` Int64,
    `company_id` Int64,
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `engineer_id`;

CREATE TABLE `assets_maintenance`.`Engineer_Skills` (
    `engineer_id` Int64,
    `skill_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`engineer_id`, `skill_id`);

CREATE TABLE `assets_maintenance`.`Fault_Log` (
    `fault_log_entry_id` Int64,
    `asset_id` Int64,
    `recorded_by_staff_id` Int64,
    `fault_log_entry_datetime` Nullable(DateTime),
    `fault_description` Nullable(String),
    `other_fault_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `fault_log_entry_id`;

CREATE TABLE `assets_maintenance`.`Engineer_Visits` (
    `engineer_visit_id` Int64,
    `contact_staff_id` Nullable(Int64),
    `engineer_id` Int64,
    `fault_log_entry_id` Int64,
    `fault_status` String,
    `visit_start_datetime` Nullable(DateTime),
    `visit_end_datetime` Nullable(DateTime),
    `other_visit_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `engineer_visit_id`;

CREATE TABLE `assets_maintenance`.`Part_Faults` (
    `part_fault_id` Int64,
    `part_id` Int64,
    `fault_short_name` Nullable(String),
    `fault_description` Nullable(String),
    `other_fault_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `part_fault_id`;

CREATE TABLE `assets_maintenance`.`Fault_Log_Parts` (
    `fault_log_entry_id` Int64,
    `part_fault_id` Int64,
    `fault_status` String
)
ENGINE = MergeTree()
ORDER BY (`fault_log_entry_id`, `part_fault_id`, `fault_status`);

CREATE TABLE `assets_maintenance`.`Skills_Required_To_Fix` (
    `part_fault_id` Int64,
    `skill_id` Int64
)
ENGINE = MergeTree()
ORDER BY (`part_fault_id`, `skill_id`);

