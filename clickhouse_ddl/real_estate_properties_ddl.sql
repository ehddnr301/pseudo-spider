-- ClickHouse DDL for database: real_estate_properties
-- Generated from: spider_data/database/real_estate_properties/real_estate_properties.sqlite

CREATE DATABASE IF NOT EXISTS real_estate_properties;

CREATE TABLE `real_estate_properties`.`Ref_Feature_Types` (
    `feature_type_code` String,
    `feature_type_name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `feature_type_code`;

CREATE TABLE `real_estate_properties`.`Ref_Property_Types` (
    `property_type_code` String,
    `property_type_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `property_type_code`;

CREATE TABLE `real_estate_properties`.`Other_Available_Features` (
    `feature_id` Int64,
    `feature_type_code` String,
    `feature_name` Nullable(String),
    `feature_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `feature_id`;

CREATE TABLE `real_estate_properties`.`Properties` (
    `property_id` Int64,
    `property_type_code` String,
    `date_on_market` Nullable(DateTime),
    `date_sold` Nullable(DateTime),
    `property_name` Nullable(String),
    `property_address` Nullable(String),
    `room_count` Nullable(Int64),
    `vendor_requested_price` Nullable(Decimal64(2)),
    `buyer_offered_price` Nullable(Decimal64(2)),
    `agreed_selling_price` Nullable(Decimal64(2)),
    `apt_feature_1` Nullable(String),
    `apt_feature_2` Nullable(String),
    `apt_feature_3` Nullable(String),
    `fld_feature_1` Nullable(String),
    `fld_feature_2` Nullable(String),
    `fld_feature_3` Nullable(String),
    `hse_feature_1` Nullable(String),
    `hse_feature_2` Nullable(String),
    `hse_feature_3` Nullable(String),
    `oth_feature_1` Nullable(String),
    `oth_feature_2` Nullable(String),
    `oth_feature_3` Nullable(String),
    `shp_feature_1` Nullable(String),
    `shp_feature_2` Nullable(String),
    `shp_feature_3` Nullable(String),
    `other_property_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `property_id`;

CREATE TABLE `real_estate_properties`.`Other_Property_Features` (
    `property_id` Int64,
    `feature_id` Int64,
    `property_feature_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY (`property_id`, `feature_id`);

