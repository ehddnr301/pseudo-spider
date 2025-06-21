-- ClickHouse DDL for database: local_govt_mdm
-- Generated from: spider_data/database/local_govt_mdm/local_govt_mdm.sqlite

CREATE DATABASE IF NOT EXISTS local_govt_mdm;

CREATE TABLE `local_govt_mdm`.`Customer_Master_Index` (
    `master_customer_id` Int64,
    `cmi_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `master_customer_id`;

CREATE TABLE `local_govt_mdm`.`CMI_Cross_References` (
    `cmi_cross_ref_id` Int64,
    `master_customer_id` Int64,
    `source_system_code` String
)
ENGINE = MergeTree()
ORDER BY `cmi_cross_ref_id`;

CREATE TABLE `local_govt_mdm`.`Council_Tax` (
    `council_tax_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `council_tax_id`;

CREATE TABLE `local_govt_mdm`.`Business_Rates` (
    `business_rates_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `business_rates_id`;

CREATE TABLE `local_govt_mdm`.`Benefits_Overpayments` (
    `council_tax_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `council_tax_id`;

CREATE TABLE `local_govt_mdm`.`Parking_Fines` (
    `council_tax_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `council_tax_id`;

CREATE TABLE `local_govt_mdm`.`Rent_Arrears` (
    `council_tax_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `council_tax_id`;

CREATE TABLE `local_govt_mdm`.`Electoral_Register` (
    `electoral_register_id` Int64,
    `cmi_cross_ref_id` Int64
)
ENGINE = MergeTree()
ORDER BY `electoral_register_id`;

