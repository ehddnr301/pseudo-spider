-- ClickHouse DDL for database: coffee_shop
-- Generated from: spider_data/database/coffee_shop/coffee_shop.sqlite

CREATE DATABASE IF NOT EXISTS coffee_shop;

CREATE TABLE `coffee_shop`.`shop` (
    `Shop_ID` Int32,
    `Address` Nullable(String),
    `Num_of_staff` Nullable(String),
    `Score` Nullable(Float64),
    `Open_Year` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Shop_ID`;

CREATE TABLE `coffee_shop`.`member` (
    `Member_ID` Int32,
    `Name` Nullable(String),
    `Membership_card` Nullable(String),
    `Age` Nullable(Int32),
    `Time_of_purchase` Nullable(Int32),
    `Level_of_membership` Nullable(Int32),
    `Address` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Member_ID`;

CREATE TABLE `coffee_shop`.`happy_hour` (
    `HH_ID` Int32,
    `Shop_ID` Int32,
    `Month` String,
    `Num_of_shaff_in_charge` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY (`HH_ID`, `Shop_ID`, `Month`);

CREATE TABLE `coffee_shop`.`happy_hour_member` (
    `HH_ID` Int32,
    `Member_ID` Int32,
    `Total_amount` Nullable(Float64)
)
ENGINE = MergeTree()
ORDER BY (`HH_ID`, `Member_ID`);

