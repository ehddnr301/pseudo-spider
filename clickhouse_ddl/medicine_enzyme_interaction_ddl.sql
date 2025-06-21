-- ClickHouse DDL for database: medicine_enzyme_interaction
-- Generated from: spider_data/database/medicine_enzyme_interaction/medicine_enzyme_interaction.sqlite

CREATE DATABASE IF NOT EXISTS medicine_enzyme_interaction;

CREATE TABLE `medicine_enzyme_interaction`.`medicine` (
    `id` Int32,
    `name` Nullable(String),
    `Trade_Name` Nullable(String),
    `FDA_approved` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `medicine_enzyme_interaction`.`enzyme` (
    `id` Int32,
    `name` Nullable(String),
    `Location` Nullable(String),
    `Product` Nullable(String),
    `Chromosome` Nullable(String),
    `OMIM` Nullable(Int32),
    `Porphyria` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `id`;

CREATE TABLE `medicine_enzyme_interaction`.`medicine_enzyme_interaction` (
    `enzyme_id` Int32,
    `medicine_id` Int32,
    `interaction_type` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`enzyme_id`, `medicine_id`);

