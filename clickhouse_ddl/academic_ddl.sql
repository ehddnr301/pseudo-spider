-- ClickHouse DDL for database: academic
-- Generated from: spider_data/database/academic/academic.sqlite

CREATE DATABASE IF NOT EXISTS academic;

CREATE TABLE `academic`.`author` (
    `aid` Int32,
    `homepage` Nullable(String),
    `name` Nullable(String),
    `oid` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `aid`;

CREATE TABLE `academic`.`conference` (
    `cid` Int32,
    `homepage` Nullable(String),
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `cid`;

CREATE TABLE `academic`.`domain` (
    `did` Int32,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `did`;

CREATE TABLE `academic`.`domain_author` (
    `aid` Int32,
    `did` Int32
)
ENGINE = MergeTree()
ORDER BY (`aid`, `did`);

CREATE TABLE `academic`.`domain_conference` (
    `cid` Int32,
    `did` Int32
)
ENGINE = MergeTree()
ORDER BY (`cid`, `did`);

CREATE TABLE `academic`.`journal` (
    `homepage` Nullable(String),
    `jid` Int32,
    `name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `jid`;

CREATE TABLE `academic`.`domain_journal` (
    `did` Int32,
    `jid` Int32
)
ENGINE = MergeTree()
ORDER BY (`did`, `jid`);

CREATE TABLE `academic`.`keyword` (
    `keyword` Nullable(String),
    `kid` Int32
)
ENGINE = MergeTree()
ORDER BY `kid`;

CREATE TABLE `academic`.`domain_keyword` (
    `did` Int32,
    `kid` Int32
)
ENGINE = MergeTree()
ORDER BY (`did`, `kid`);

CREATE TABLE `academic`.`publication` (
    `abstract` Nullable(String),
    `cid` Nullable(String),
    `citation_num` Nullable(Int32),
    `jid` Nullable(Int32),
    `pid` Int32,
    `reference_num` Nullable(Int32),
    `title` Nullable(String),
    `year` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY `pid`;

CREATE TABLE `academic`.`domain_publication` (
    `did` Int32,
    `pid` Int32
)
ENGINE = MergeTree()
ORDER BY (`did`, `pid`);

CREATE TABLE `academic`.`organization` (
    `continent` Nullable(String),
    `homepage` Nullable(String),
    `name` Nullable(String),
    `oid` Int32
)
ENGINE = MergeTree()
ORDER BY `oid`;

CREATE TABLE `academic`.`publication_keyword` (
    `pid` Int32,
    `kid` Int32
)
ENGINE = MergeTree()
ORDER BY (`pid`, `kid`);

CREATE TABLE `academic`.`writes` (
    `aid` Int32,
    `pid` Int32
)
ENGINE = MergeTree()
ORDER BY (`aid`, `pid`);

CREATE TABLE `academic`.`cite` (
    `cited` Nullable(Int32),
    `citing` Nullable(Int32)
)
ENGINE = MergeTree()
ORDER BY tuple();

