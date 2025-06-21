-- ClickHouse DDL for database: protein_institute
-- Generated from: spider_data/database/protein_institute/protein_institute.sqlite

CREATE DATABASE IF NOT EXISTS protein_institute;

CREATE TABLE `protein_institute`.`building` (
    `building_id` String,
    `Name` Nullable(String),
    `Street_address` Nullable(String),
    `Years_as_tallest` Nullable(String),
    `Height_feet` Nullable(Int32),
    `Floors` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `building_id`;

CREATE TABLE `protein_institute`.`Institution` (
    `Institution_id` String,
    `Institution` Nullable(String),
    `Location` Nullable(String),
    `Founded` Nullable(Float64),
    `Type` Nullable(String),
    `Enrollment` Nullable(Int32),
    `Team` Nullable(String),
    `Primary_Conference` Nullable(String),
    `building_id` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Institution_id`;

CREATE TABLE `protein_institute`.`protein` (
    `common_name` String,
    `protein_name` Nullable(String),
    `divergence_from_human_lineage` Nullable(Float64),
    `accession_number` Nullable(String),
    `sequence_length` Nullable(Float64),
    `sequence_identity_to_human_protein` Nullable(String),
    `Institution_id` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `common_name`;

