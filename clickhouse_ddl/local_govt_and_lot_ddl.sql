-- ClickHouse DDL for database: local_govt_and_lot
-- Generated from: spider_data/database/local_govt_and_lot/local_govt_and_lot.sqlite

CREATE DATABASE IF NOT EXISTS local_govt_and_lot;

CREATE TABLE `local_govt_and_lot`.`Customers` (
    `customer_id` Int64,
    `customer_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `customer_id`;

CREATE TABLE `local_govt_and_lot`.`Properties` (
    `property_id` Int64,
    `property_type_code` String,
    `property_address` Nullable(String),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `property_id`;

CREATE TABLE `local_govt_and_lot`.`Residents` (
    `resident_id` Int64,
    `property_id` Int64,
    `date_moved_in` DateTime,
    `date_moved_out` DateTime,
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`resident_id`, `property_id`, `date_moved_in`);

CREATE TABLE `local_govt_and_lot`.`Organizations` (
    `organization_id` Int64,
    `parent_organization_id` Nullable(Int64),
    `organization_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `organization_id`;

CREATE TABLE `local_govt_and_lot`.`Services` (
    `service_id` Int64,
    `organization_id` Int64,
    `service_type_code` String,
    `service_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `service_id`;

CREATE TABLE `local_govt_and_lot`.`Residents_Services` (
    `resident_id` Int64,
    `service_id` Int64,
    `date_moved_in` Nullable(DateTime),
    `property_id` Nullable(Int64),
    `date_requested` Nullable(DateTime),
    `date_provided` Nullable(DateTime),
    `other_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`resident_id`, `service_id`);

CREATE TABLE `local_govt_and_lot`.`Things` (
    `thing_id` Int64,
    `organization_id` Int64,
    `Type_of_Thing_Code` String,
    `service_type_code` String,
    `service_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `thing_id`;

CREATE TABLE `local_govt_and_lot`.`Customer_Events` (
    `Customer_Event_ID` Int64,
    `customer_id` Nullable(Int64),
    `date_moved_in` Nullable(DateTime),
    `property_id` Nullable(Int64),
    `resident_id` Nullable(Int64),
    `thing_id` Int64
)
ENGINE = MergeTree()
ORDER BY `Customer_Event_ID`;

CREATE TABLE `local_govt_and_lot`.`Customer_Event_Notes` (
    `Customer_Event_Note_ID` Int64,
    `Customer_Event_ID` Int64,
    `service_type_code` String,
    `resident_id` Int64,
    `property_id` Int64,
    `date_moved_in` DateTime
)
ENGINE = MergeTree()
ORDER BY `Customer_Event_Note_ID`;

CREATE TABLE `local_govt_and_lot`.`Timed_Status_of_Things` (
    `thing_id` Int64,
    `Date_and_Date` DateTime,
    `Status_of_Thing_Code` String
)
ENGINE = MergeTree()
ORDER BY (`thing_id`, `Date_and_Date`, `Status_of_Thing_Code`);

CREATE TABLE `local_govt_and_lot`.`Timed_Locations_of_Things` (
    `thing_id` Int64,
    `Date_and_Time` DateTime,
    `Location_Code` String
)
ENGINE = MergeTree()
ORDER BY (`thing_id`, `Date_and_Time`, `Location_Code`);

