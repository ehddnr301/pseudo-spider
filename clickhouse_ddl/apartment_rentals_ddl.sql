-- ClickHouse DDL for database: apartment_rentals
-- Generated from: spider_data/database/apartment_rentals/apartment_rentals.sqlite

CREATE DATABASE IF NOT EXISTS apartment_rentals;

CREATE TABLE `apartment_rentals`.`Apartment_Buildings` (
    `building_id` Int64,
    `building_short_name` Nullable(String),
    `building_full_name` Nullable(String),
    `building_description` Nullable(String),
    `building_address` Nullable(String),
    `building_manager` Nullable(String),
    `building_phone` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `building_id`;

CREATE TABLE `apartment_rentals`.`Apartments` (
    `apt_id` Int64,
    `building_id` Int64,
    `apt_type_code` Nullable(String),
    `apt_number` Nullable(String),
    `bathroom_count` Nullable(Int64),
    `bedroom_count` Nullable(Int64),
    `room_count` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `apt_id`;

CREATE TABLE `apartment_rentals`.`Apartment_Facilities` (
    `apt_id` Int64,
    `facility_code` String
)
ENGINE = MergeTree()
ORDER BY (`apt_id`, `facility_code`);

CREATE TABLE `apartment_rentals`.`Guests` (
    `guest_id` Int64,
    `gender_code` Nullable(String),
    `guest_first_name` Nullable(String),
    `guest_last_name` Nullable(String),
    `date_of_birth` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `guest_id`;

CREATE TABLE `apartment_rentals`.`Apartment_Bookings` (
    `apt_booking_id` Int64,
    `apt_id` Nullable(Int64),
    `guest_id` Int64,
    `booking_status_code` String,
    `booking_start_date` Nullable(DateTime),
    `booking_end_date` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `apt_booking_id`;

CREATE TABLE `apartment_rentals`.`View_Unit_Status` (
    `apt_id` Nullable(Int64),
    `apt_booking_id` Nullable(Int64),
    `status_date` DateTime,
    `available_yn` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `status_date`;

