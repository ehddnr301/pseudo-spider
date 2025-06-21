-- ClickHouse DDL for database: college_1
-- Generated from: spider_data/database/college_1/college_1.sqlite

CREATE DATABASE IF NOT EXISTS college_1;

CREATE TABLE `college_1`.`CLASS` (
    `CLASS_CODE` String,
    `CRS_CODE` Nullable(String),
    `CLASS_SECTION` Nullable(String),
    `CLASS_TIME` Nullable(String),
    `CLASS_ROOM` Nullable(String),
    `PROF_NUM` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `CLASS_CODE`;

CREATE TABLE `college_1`.`COURSE` (
    `CRS_CODE` String,
    `DEPT_CODE` Nullable(String),
    `CRS_DESCRIPTION` Nullable(String),
    `CRS_CREDIT` Nullable(Float32)
)
ENGINE = MergeTree()
ORDER BY `CRS_CODE`;

CREATE TABLE `college_1`.`DEPARTMENT` (
    `DEPT_CODE` String,
    `DEPT_NAME` Nullable(String),
    `SCHOOL_CODE` Nullable(String),
    `EMP_NUM` Nullable(Int32),
    `DEPT_ADDRESS` Nullable(String),
    `DEPT_EXTENSION` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `DEPT_CODE`;

CREATE TABLE `college_1`.`EMPLOYEE` (
    `EMP_NUM` Int32,
    `EMP_LNAME` Nullable(String),
    `EMP_FNAME` Nullable(String),
    `EMP_INITIAL` Nullable(String),
    `EMP_JOBCODE` Nullable(String),
    `EMP_HIREDATE` Nullable(DateTime),
    `EMP_DOB` Nullable(DateTime)
)
ENGINE = MergeTree()
ORDER BY `EMP_NUM`;

CREATE TABLE `college_1`.`ENROLL` (
    `CLASS_CODE` Nullable(String),
    `STU_NUM` Nullable(Int32),
    `ENROLL_GRADE` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `college_1`.`PROFESSOR` (
    `EMP_NUM` Nullable(Int32),
    `DEPT_CODE` Nullable(String),
    `PROF_OFFICE` Nullable(String),
    `PROF_EXTENSION` Nullable(String),
    `PROF_HIGH_DEGREE` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE `college_1`.`STUDENT` (
    `STU_NUM` Int32,
    `STU_LNAME` Nullable(String),
    `STU_FNAME` Nullable(String),
    `STU_INIT` Nullable(String),
    `STU_DOB` Nullable(DateTime),
    `STU_HRS` Nullable(Int32),
    `STU_CLASS` Nullable(String),
    `STU_GPA` Nullable(Float32),
    `STU_TRANSFER` Nullable(Decimal64(2)),
    `DEPT_CODE` Nullable(String),
    `STU_PHONE` Nullable(String),
    `PROF_NUM` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `STU_NUM`;

