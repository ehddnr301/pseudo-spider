-- ClickHouse DDL for database: inn_1
-- Generated from: spider_data/database/inn_1/inn_1.sqlite

CREATE DATABASE IF NOT EXISTS inn_1;

CREATE TABLE `inn_1`.`Rooms` (
    `RoomId` String,
    `roomName` Nullable(String),
    `beds` Nullable(Int64),
    `bedType` Nullable(String),
    `maxOccupancy` Nullable(Int64),
    `basePrice` Nullable(Int64),
    `decor` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `RoomId`;

CREATE TABLE `inn_1`.`Reservations` (
    `Code` Int64,
    `Room` Nullable(String),
    `CheckIn` Nullable(String),
    `CheckOut` Nullable(String),
    `Rate` Nullable(Float64),
    `LastName` Nullable(String),
    `FirstName` Nullable(String),
    `Adults` Nullable(Int64),
    `Kids` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `Code`;

