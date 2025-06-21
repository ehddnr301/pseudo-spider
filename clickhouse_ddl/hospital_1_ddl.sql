-- ClickHouse DDL for database: hospital_1
-- Generated from: spider_data/database/hospital_1/hospital_1.sqlite

CREATE DATABASE IF NOT EXISTS hospital_1;

CREATE TABLE `hospital_1`.`Physician` (
    `EmployeeID` Int64,
    `Name` String,
    `Position` String,
    `SSN` Int64
)
ENGINE = MergeTree()
ORDER BY `EmployeeID`;

CREATE TABLE `hospital_1`.`Department` (
    `DepartmentID` Int64,
    `Name` String,
    `Head` Int64
)
ENGINE = MergeTree()
ORDER BY `DepartmentID`;

CREATE TABLE `hospital_1`.`Affiliated_With` (
    `Physician` Int64,
    `Department` Int64,
    `PrimaryAffiliation` UInt8
)
ENGINE = MergeTree()
ORDER BY (`Physician`, `Department`);

CREATE TABLE `hospital_1`.`Procedures` (
    `Code` Int64,
    `Name` String,
    `Cost` Float64
)
ENGINE = MergeTree()
ORDER BY `Code`;

CREATE TABLE `hospital_1`.`Trained_In` (
    `Physician` Int64,
    `Treatment` Int64,
    `CertificationDate` DateTime,
    `CertificationExpires` DateTime
)
ENGINE = MergeTree()
ORDER BY (`Physician`, `Treatment`);

CREATE TABLE `hospital_1`.`Patient` (
    `SSN` Int64,
    `Name` String,
    `Address` String,
    `Phone` String,
    `InsuranceID` Int64,
    `PCP` Int64
)
ENGINE = MergeTree()
ORDER BY `SSN`;

CREATE TABLE `hospital_1`.`Nurse` (
    `EmployeeID` Int64,
    `Name` String,
    `Position` String,
    `Registered` UInt8,
    `SSN` Int64
)
ENGINE = MergeTree()
ORDER BY `EmployeeID`;

CREATE TABLE `hospital_1`.`Appointment` (
    `AppointmentID` Int64,
    `Patient` Int64,
    `PrepNurse` Nullable(Int64),
    `Physician` Int64,
    `Start` DateTime,
    `End` DateTime,
    `ExaminationRoom` String
)
ENGINE = MergeTree()
ORDER BY `AppointmentID`;

CREATE TABLE `hospital_1`.`Medication` (
    `Code` Int64,
    `Name` String,
    `Brand` String,
    `Description` String
)
ENGINE = MergeTree()
ORDER BY `Code`;

CREATE TABLE `hospital_1`.`Prescribes` (
    `Physician` Int64,
    `Patient` Int64,
    `Medication` Int64,
    `Date` DateTime,
    `Appointment` Nullable(Int64),
    `Dose` String
)
ENGINE = MergeTree()
ORDER BY (`Physician`, `Patient`, `Medication`, `Date`);

CREATE TABLE `hospital_1`.`Block` (
    `BlockFloor` Int64,
    `BlockCode` Int64
)
ENGINE = MergeTree()
ORDER BY (`BlockFloor`, `BlockCode`);

CREATE TABLE `hospital_1`.`Room` (
    `RoomNumber` Int64,
    `RoomType` String,
    `BlockFloor` Int64,
    `BlockCode` Int64,
    `Unavailable` UInt8
)
ENGINE = MergeTree()
ORDER BY `RoomNumber`;

CREATE TABLE `hospital_1`.`On_Call` (
    `Nurse` Int64,
    `BlockFloor` Int64,
    `BlockCode` Int64,
    `OnCallStart` DateTime,
    `OnCallEnd` DateTime
)
ENGINE = MergeTree()
ORDER BY (`Nurse`, `BlockFloor`, `BlockCode`, `OnCallStart`, `OnCallEnd`);

CREATE TABLE `hospital_1`.`Stay` (
    `StayID` Int64,
    `Patient` Int64,
    `Room` Int64,
    `StayStart` DateTime,
    `StayEnd` DateTime
)
ENGINE = MergeTree()
ORDER BY `StayID`;

CREATE TABLE `hospital_1`.`Undergoes` (
    `Patient` Int64,
    `Procedures` Int64,
    `Stay` Int64,
    `DateUndergoes` DateTime,
    `Physician` Int64,
    `AssistingNurse` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY (`Patient`, `Procedures`, `Stay`, `DateUndergoes`);

