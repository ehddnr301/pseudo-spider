-- ClickHouse DDL for database: scholar
-- Generated from: spider_data/database/scholar/scholar.sqlite

CREATE DATABASE IF NOT EXISTS scholar;

CREATE TABLE `scholar`.`venue` (
    `venueId` Int64,
    `venueName` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `venueId`;

CREATE TABLE `scholar`.`author` (
    `authorId` Int64,
    `authorName` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `authorId`;

CREATE TABLE `scholar`.`dataset` (
    `datasetId` Int64,
    `datasetName` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `datasetId`;

CREATE TABLE `scholar`.`journal` (
    `journalId` Int64,
    `journalName` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `journalId`;

CREATE TABLE `scholar`.`keyphrase` (
    `keyphraseId` Int64,
    `keyphraseName` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `keyphraseId`;

CREATE TABLE `scholar`.`paper` (
    `paperId` Int64,
    `title` Nullable(String),
    `venueId` Nullable(Int64),
    `year` Nullable(Int64),
    `numCiting` Nullable(Int64),
    `numCitedBy` Nullable(Int64),
    `journalId` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `paperId`;

CREATE TABLE `scholar`.`cite` (
    `citingPaperId` Int64,
    `citedPaperId` Int64
)
ENGINE = MergeTree()
ORDER BY (`citingPaperId`, `citedPaperId`);

CREATE TABLE `scholar`.`paperDataset` (
    `paperId` Int64,
    `datasetId` Int64
)
ENGINE = MergeTree()
ORDER BY (`paperId`, `datasetId`);

CREATE TABLE `scholar`.`paperKeyphrase` (
    `paperId` Int64,
    `keyphraseId` Int64
)
ENGINE = MergeTree()
ORDER BY (`paperId`, `keyphraseId`);

CREATE TABLE `scholar`.`writes` (
    `paperId` Int64,
    `authorId` Int64
)
ENGINE = MergeTree()
ORDER BY (`paperId`, `authorId`);

