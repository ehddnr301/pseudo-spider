-- ClickHouse DDL for database: sakila_1
-- Generated from: spider_data/database/sakila_1/sakila_1.sqlite

CREATE DATABASE IF NOT EXISTS sakila_1;

CREATE TABLE `sakila_1`.`actor` (
    `actor_id` Int16,
    `first_name` String,
    `last_name` String,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `actor_id`;

CREATE TABLE `sakila_1`.`address` (
    `address_id` Int16,
    `address` String,
    `address2` Nullable(String),
    `district` String,
    `city_id` Int16,
    `postal_code` Nullable(String),
    `phone` String,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `address_id`;

CREATE TABLE `sakila_1`.`category` (
    `category_id` Int8,
    `name` String,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `category_id`;

CREATE TABLE `sakila_1`.`city` (
    `city_id` Int16,
    `city` String,
    `country_id` Int16,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `city_id`;

CREATE TABLE `sakila_1`.`country` (
    `country_id` Int16,
    `country` String,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `country_id`;

CREATE TABLE `sakila_1`.`customer` (
    `customer_id` Int16,
    `store_id` Int8,
    `first_name` String,
    `last_name` String,
    `email` Nullable(String),
    `address_id` Int16,
    `active` UInt8 DEFAULT TRUE,
    `create_date` DateTime,
    `last_update` Nullable(DateTime) DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `sakila_1`.`film` (
    `film_id` Int16,
    `title` String,
    `description` Nullable(String),
    `release_year` Nullable(String),
    `language_id` Int8,
    `original_language_id` Nullable(Int8),
    `rental_duration` Int8 DEFAULT 3,
    `rental_rate` Decimal64(2) DEFAULT 4.99,
    `length` Nullable(Int16),
    `replacement_cost` Decimal64(2) DEFAULT 19.99,
    `rating` Nullable(String) DEFAULT 'G',
    `special_features` Nullable(String),
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `film_id`;

CREATE TABLE `sakila_1`.`film_actor` (
    `actor_id` Int16,
    `film_id` Int16,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY (`actor_id`, `film_id`);

CREATE TABLE `sakila_1`.`film_category` (
    `film_id` Int16,
    `category_id` Int8,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY (`film_id`, `category_id`);

CREATE TABLE `sakila_1`.`film_text` (
    `film_id` Int16,
    `title` String,
    `description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `film_id`;

CREATE TABLE `sakila_1`.`inventory` (
    `inventory_id` String,
    `film_id` Int16,
    `store_id` Int8,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `inventory_id`;

CREATE TABLE `sakila_1`.`language` (
    `language_id` Int8,
    `name` String,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `language_id`;

CREATE TABLE `sakila_1`.`payment` (
    `payment_id` Int16,
    `customer_id` Int16,
    `staff_id` Int8,
    `rental_id` Nullable(Int32),
    `amount` Decimal64(2),
    `payment_date` DateTime,
    `last_update` Nullable(DateTime) DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `payment_id`;

CREATE TABLE `sakila_1`.`rental` (
    `rental_id` Int32,
    `rental_date` DateTime,
    `inventory_id` String,
    `customer_id` Int16,
    `return_date` Nullable(DateTime),
    `staff_id` Int8,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `rental_id`;

CREATE TABLE `sakila_1`.`staff` (
    `staff_id` Int8,
    `first_name` String,
    `last_name` String,
    `address_id` Int16,
    `picture` Nullable(String),
    `email` Nullable(String),
    `store_id` Int8,
    `active` UInt8 DEFAULT TRUE,
    `username` String,
    `password` Nullable(String),
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `staff_id`;

CREATE TABLE `sakila_1`.`store` (
    `store_id` Int8,
    `manager_staff_id` Int8,
    `address_id` Int16,
    `last_update` DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY `store_id`;

