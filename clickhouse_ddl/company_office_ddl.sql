-- ClickHouse DDL for database: company_office
-- Generated from: spider_data/database/company_office/company_office.sqlite

CREATE DATABASE IF NOT EXISTS company_office;

CREATE TABLE `company_office`.`buildings` (
    `id` Int32,
    `name` Nullable(String),
    `City` Nullable(String),
    `Height` Nullable(Int32),
    `Stories` Nullable(Int32),
    `Status` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `company_office`.`Companies` (
    `id` Int32,
    `name` Nullable(String),
    `Headquarters` Nullable(String),
    `Industry` Nullable(String),
    `Sales_billion` Nullable(Float64),
    `Profits_billion` Nullable(Float64),
    `Assets_billion` Nullable(Float64),
    `Market_Value_billion` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `company_office`.`Office_locations` (
    `building_id` Int32,
    `company_id` Int32,
    `move_in_year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`building_id`, `company_id`);

