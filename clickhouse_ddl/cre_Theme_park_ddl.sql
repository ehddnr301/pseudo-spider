-- ClickHouse DDL for database: cre_Theme_park
-- Generated from: spider_data/database/cre_Theme_park/cre_Theme_park.sqlite

CREATE DATABASE IF NOT EXISTS cre_Theme_park;

CREATE TABLE `cre_Theme_park`.`Ref_Hotel_Star_Ratings` (
    `star_rating_code` String,
    `star_rating_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `star_rating_code`;

CREATE TABLE `cre_Theme_park`.`Locations` (
    `Location_ID` Int64,
    `Location_Name` Nullable(String),
    `Address` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Location_ID`;

CREATE TABLE `cre_Theme_park`.`Ref_Attraction_Types` (
    `Attraction_Type_Code` String,
    `Attraction_Type_Description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Attraction_Type_Code`;

CREATE TABLE `cre_Theme_park`.`Visitors` (
    `Tourist_ID` Int64,
    `Tourist_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Tourist_ID`;

CREATE TABLE `cre_Theme_park`.`Features` (
    `Feature_ID` Int64,
    `Feature_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Feature_ID`;

CREATE TABLE `cre_Theme_park`.`Hotels` (
    `hotel_id` Int64,
    `star_rating_code` String,
    `pets_allowed_yn` Nullable(String),
    `price_range` Nullable(Float64),
    `other_hotel_details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `hotel_id`;

CREATE TABLE `cre_Theme_park`.`Tourist_Attractions` (
    `Tourist_Attraction_ID` Int64,
    `Attraction_Type_Code` String,
    `Location_ID` Int64,
    `How_to_Get_There` Nullable(String),
    `Name` Nullable(String),
    `Description` Nullable(String),
    `Opening_Hours` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Tourist_Attraction_ID`;

CREATE TABLE `cre_Theme_park`.`Street_Markets` (
    `Market_ID` Int64,
    `Market_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Market_ID`;

CREATE TABLE `cre_Theme_park`.`Shops` (
    `Shop_ID` Int64,
    `Shop_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Shop_ID`;

CREATE TABLE `cre_Theme_park`.`Museums` (
    `Museum_ID` Int64,
    `Museum_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Museum_ID`;

CREATE TABLE `cre_Theme_park`.`Royal_Family` (
    `Royal_Family_ID` Int64,
    `Royal_Family_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Royal_Family_ID`;

CREATE TABLE `cre_Theme_park`.`Theme_Parks` (
    `Theme_Park_ID` Int64,
    `Theme_Park_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Theme_Park_ID`;

CREATE TABLE `cre_Theme_park`.`Visits` (
    `Visit_ID` Int64,
    `Tourist_Attraction_ID` Int64,
    `Tourist_ID` Int64,
    `Visit_Date` DateTime,
    `Visit_Details` String
)
ENGINE = MergeTree()
ORDER BY `Visit_ID`;

CREATE TABLE `cre_Theme_park`.`Photos` (
    `Photo_ID` Int64,
    `Tourist_Attraction_ID` Int64,
    `Name` Nullable(String),
    `Description` Nullable(String),
    `Filename` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Photo_ID`;

CREATE TABLE `cre_Theme_park`.`Staff` (
    `Staff_ID` Int64,
    `Tourist_Attraction_ID` Int64,
    `Name` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Staff_ID`;

CREATE TABLE `cre_Theme_park`.`Tourist_Attraction_Features` (
    `Tourist_Attraction_ID` Int64,
    `Feature_ID` Int64
)
ENGINE = MergeTree()
ORDER BY (`Tourist_Attraction_ID`, `Feature_ID`);

