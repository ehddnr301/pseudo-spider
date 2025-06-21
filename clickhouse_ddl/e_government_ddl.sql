-- ClickHouse DDL for database: e_government
-- Generated from: spider_data/database/e_government/e_government.sqlite

CREATE DATABASE IF NOT EXISTS e_government;

CREATE TABLE `e_government`.`Addresses` (
    `address_id` Int64,
    `line_1_number_building` Nullable(String),
    `town_city` Nullable(String),
    `zip_postcode` Nullable(String),
    `state_province_county` Nullable(String),
    `country` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `e_government`.`Services` (
    `service_id` Int64,
    `service_type_code` String,
    `service_name` Nullable(String),
    `service_descriptio` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `service_id`;

CREATE TABLE `e_government`.`Forms` (
    `form_id` Int64,
    `form_type_code` String,
    `service_id` Nullable(Int64),
    `form_number` Nullable(String),
    `form_name` Nullable(String),
    `form_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `form_id`;

CREATE TABLE `e_government`.`Individuals` (
    `individual_id` Int64,
    `individual_first_name` Nullable(String),
    `individual_middle_name` Nullable(String),
    `inidividual_phone` Nullable(String),
    `individual_email` Nullable(String),
    `individual_address` Nullable(String),
    `individual_last_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `individual_id`;

CREATE TABLE `e_government`.`Organizations` (
    `organization_id` Int64,
    `date_formed` Nullable(DateTime),
    `organization_name` Nullable(String),
    `uk_vat_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `organization_id`;

CREATE TABLE `e_government`.`Parties` (
    `party_id` Int64,
    `payment_method_code` String,
    `party_phone` Nullable(String),
    `party_email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `party_id`;

CREATE TABLE `e_government`.`Organization_Contact_Individuals` (
    `individual_id` Int64,
    `organization_id` Int64,
    `date_contact_from` DateTime,
    `date_contact_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`individual_id`, `organization_id`);

CREATE TABLE `e_government`.`Party_Addresses` (
    `party_id` Int64,
    `address_id` Int64,
    `date_address_from` DateTime,
    `address_type_code` String,
    `date_address_to` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`party_id`, `address_id`);

CREATE TABLE `e_government`.`Party_Forms` (
    `party_id` Int64,
    `form_id` Int64,
    `date_completion_started` DateTime,
    `form_status_code` String,
    `date_fully_completed` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`party_id`, `form_id`);

CREATE TABLE `e_government`.`Party_Services` (
    `booking_id` Int64,
    `customer_id` Int64,
    `service_id` Int64,
    `service_datetime` DateTime,
    `booking_made_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY (`booking_id`, `customer_id`, `service_id`, `service_datetime`);

