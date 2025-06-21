-- ClickHouse DDL for database: small_bank_1
-- Generated from: spider_data/database/small_bank_1/small_bank_1.sqlite

CREATE DATABASE IF NOT EXISTS small_bank_1;

CREATE TABLE `small_bank_1`.`ACCOUNTS` (
    `custid` Int64,
    `name` String
)
ENGINE = MergeTree()
ORDER BY `custid`;

CREATE TABLE `small_bank_1`.`SAVINGS` (
    `custid` Int64,
    `balance` Float32
)
ENGINE = MergeTree()
ORDER BY `custid`;

CREATE TABLE `small_bank_1`.`CHECKING` (
    `custid` Int64,
    `balance` Float32
)
ENGINE = MergeTree()
ORDER BY `custid`;

