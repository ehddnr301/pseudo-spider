-- ClickHouse DDL for database: shop_membership
-- Generated from: spider_data/database/shop_membership/shop_membership.sqlite

CREATE DATABASE IF NOT EXISTS shop_membership;

CREATE TABLE `shop_membership`.`member` (
    `Member_ID` Int32,
    `Card_Number` Nullable(String),
    `Name` Nullable(String),
    `Hometown` Nullable(String),
    `Level` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `shop_membership`.`branch` (
    `Branch_ID` Int32,
    `Name` Nullable(String),
    `Open_year` Nullable(String),
    `Address_road` Nullable(String),
    `City` Nullable(String),
    `membership_amount` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Branch_ID`;

CREATE TABLE `shop_membership`.`membership_register_branch` (
    `Member_ID` Int32,
    `Branch_ID` Nullable(String),
    `Register_Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `shop_membership`.`purchase` (
    `Member_ID` Int32,
    `Branch_ID` String,
    `Year` String,
    `Total_pounds` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`Member_ID`, `Branch_ID`, `Year`);

