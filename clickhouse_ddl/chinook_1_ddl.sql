-- ClickHouse DDL for database: chinook_1
-- Generated from: spider_data/database/chinook_1/chinook_1.sqlite

CREATE DATABASE IF NOT EXISTS chinook_1;

CREATE TABLE `chinook_1`.`Album` (
    `AlbumId` Int64,
    `Title` String,
    `ArtistId` Int64
)
ENGINE = MergeTree()
ORDER BY `AlbumId`;

CREATE TABLE `chinook_1`.`Artist` (
    `ArtistId` Int64,
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `ArtistId`;

CREATE TABLE `chinook_1`.`Customer` (
    `CustomerId` Int64,
    `FirstName` String,
    `LastName` String,
    `Company` Nullable(String),
    `Address` Nullable(String),
    `City` Nullable(String),
    `State` Nullable(String),
    `Country` Nullable(String),
    `PostalCode` Nullable(String),
    `Phone` Nullable(String),
    `Fax` Nullable(String),
    `Email` String,
    `SupportRepId` Nullable(Int64)
)
ENGINE = MergeTree()
ORDER BY `CustomerId`;

CREATE TABLE `chinook_1`.`Employee` (
    `EmployeeId` Int64,
    `LastName` String,
    `FirstName` String,
    `Title` Nullable(String),
    `ReportsTo` Nullable(Int64),
    `BirthDate` Nullable(DateTime),
    `HireDate` Nullable(DateTime),
    `Address` Nullable(String),
    `City` Nullable(String),
    `State` Nullable(String),
    `Country` Nullable(String),
    `PostalCode` Nullable(String),
    `Phone` Nullable(String),
    `Fax` Nullable(String),
    `Email` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `EmployeeId`;

CREATE TABLE `chinook_1`.`Genre` (
    `GenreId` Int64,
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `GenreId`;

CREATE TABLE `chinook_1`.`Invoice` (
    `InvoiceId` Int64,
    `CustomerId` Int64,
    `InvoiceDate` DateTime,
    `BillingAddress` Nullable(String),
    `BillingCity` Nullable(String),
    `BillingState` Nullable(String),
    `BillingCountry` Nullable(String),
    `BillingPostalCode` Nullable(String),
    `Total` Decimal64(2)
)
ENGINE = MergeTree()
ORDER BY `InvoiceId`;

CREATE TABLE `chinook_1`.`InvoiceLine` (
    `InvoiceLineId` Int64,
    `InvoiceId` Int64,
    `TrackId` Int64,
    `UnitPrice` Decimal64(2),
    `Quantity` Int64
)
ENGINE = MergeTree()
ORDER BY `InvoiceLineId`;

CREATE TABLE `chinook_1`.`MediaType` (
    `MediaTypeId` Int64,
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `MediaTypeId`;

CREATE TABLE `chinook_1`.`Playlist` (
    `PlaylistId` Int64,
    `Name` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `PlaylistId`;

CREATE TABLE `chinook_1`.`PlaylistTrack` (
    `PlaylistId` Int64,
    `TrackId` Int64
)
ENGINE = MergeTree()
ORDER BY (`PlaylistId`, `TrackId`);

CREATE TABLE `chinook_1`.`Track` (
    `TrackId` Int64,
    `Name` String,
    `AlbumId` Nullable(Int64),
    `MediaTypeId` Int64,
    `GenreId` Nullable(Int64),
    `Composer` Nullable(String),
    `Milliseconds` Int64,
    `Bytes` Nullable(Int64),
    `UnitPrice` Decimal64(2)
)
ENGINE = MergeTree()
ORDER BY `TrackId`;

