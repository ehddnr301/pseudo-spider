-- ClickHouse DDL for database: local_govt_in_alabama
-- Generated from: spider_data/database/local_govt_in_alabama/local_govt_in_alabama.sqlite

CREATE DATABASE IF NOT EXISTS local_govt_in_alabama;

CREATE TABLE `local_govt_in_alabama`.`Services` (
    `Service_ID` Int64,
    `Service_Type_Code` String
)
ENGINE = MergeTree()
ORDER BY `Service_ID`;

CREATE TABLE `local_govt_in_alabama`.`Participants` (
    `Participant_ID` Int64,
    `Participant_Type_Code` String,
    `Participant_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Participant_ID`;

CREATE TABLE `local_govt_in_alabama`.`Events` (
    `Event_ID` Int64,
    `Service_ID` Int64,
    `Event_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Event_ID`;

CREATE TABLE `local_govt_in_alabama`.`Participants_in_Events` (
    `Event_ID` Int64,
    `Participant_ID` Int64
)
ENGINE = MergeTree()
ORDER BY (`Event_ID`, `Participant_ID`);

