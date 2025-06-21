-- ClickHouse DDL for database: dog_kennels
-- Generated from: spider_data/database/dog_kennels/dog_kennels.sqlite

CREATE DATABASE IF NOT EXISTS dog_kennels;

CREATE TABLE `dog_kennels`.`Breeds` (
    `breed_code` String,
    `breed_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `breed_code`;

CREATE TABLE `dog_kennels`.`Charges` (
    `charge_id` Int64,
    `charge_type` Nullable(String),
    `charge_amount` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `charge_id`;

CREATE TABLE `dog_kennels`.`Sizes` (
    `size_code` String,
    `size_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `size_code`;

CREATE TABLE `dog_kennels`.`Treatment_Types` (
    `treatment_type_code` String,
    `treatment_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `treatment_type_code`;

CREATE TABLE `dog_kennels`.`Owners` (
    `owner_id` Int64,
    `first_name` Nullable(String),
    `last_name` Nullable(String),
    `street` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `zip_code` Nullable(String),
    `email_address` Nullable(String),
    `home_phone` Nullable(String),
    `cell_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `owner_id`;

CREATE TABLE `dog_kennels`.`Dogs` (
    `dog_id` Int64,
    `owner_id` Int64,
    `abandoned_yn` Nullable(String),
    `breed_code` String,
    `size_code` String,
    `name` Nullable(String),
    `age` Nullable(String),
    `date_of_birth` Nullable(DateTime),
    `gender` Nullable(String),
    `weight` Nullable(String),
    `date_arrived` Nullable(DateTime),
    `date_adopted` Nullable(DateTime),
    `date_departed` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `dog_id`;

CREATE TABLE `dog_kennels`.`Professionals` (
    `professional_id` Int64,
    `role_code` String,
    `first_name` Nullable(String),
    `street` Nullable(String),
    `city` Nullable(String),
    `state` Nullable(String),
    `zip_code` Nullable(String),
    `last_name` Nullable(String),
    `email_address` Nullable(String),
    `home_phone` Nullable(String),
    `cell_number` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `professional_id`;

CREATE TABLE `dog_kennels`.`Treatments` (
    `treatment_id` Int64,
    `dog_id` Int64,
    `professional_id` Int64,
    `treatment_type_code` String,
    `date_of_treatment` Nullable(DateTime),
    `cost_of_treatment` Nullable(Decimal64(2))
)
ENGINE = MergeTree()
ORDER BY `treatment_id`;

