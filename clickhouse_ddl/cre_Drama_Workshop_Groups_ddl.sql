-- ClickHouse DDL for database: cre_Drama_Workshop_Groups
-- Generated from: spider_data/database/cre_Drama_Workshop_Groups/cre_Drama_Workshop_Groups.sqlite

CREATE DATABASE IF NOT EXISTS cre_Drama_Workshop_Groups;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Ref_Payment_Methods` (
    `payment_method_code` String,
    `payment_method_description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `payment_method_code`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Ref_Service_Types` (
    `Service_Type_Code` String,
    `Parent_Service_Type_Code` Nullable(String),
    `Service_Type_Description` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Service_Type_Code`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Addresses` (
    `Address_ID` String,
    `Line_1` Nullable(String),
    `Line_2` Nullable(String),
    `City_Town` Nullable(String),
    `State_County` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Address_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Products` (
    `Product_ID` String,
    `Product_Name` Nullable(String),
    `Product_Price` Nullable(Decimal64(2)),
    `Product_Description` Nullable(String),
    `Other_Product_Service_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Product_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Marketing_Regions` (
    `Marketing_Region_Code` String,
    `Marketing_Region_Name` String,
    `Marketing_Region_Descriptrion` String,
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Marketing_Region_Code`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Clients` (
    `Client_ID` Int64,
    `Address_ID` Int64,
    `Customer_Email_Address` Nullable(String),
    `Customer_Name` Nullable(String),
    `Customer_Phone` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Client_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Drama_Workshop_Groups` (
    `Workshop_Group_ID` Int64,
    `Address_ID` Int64,
    `Currency_Code` String,
    `Marketing_Region_Code` String,
    `Store_Name` Nullable(String),
    `Store_Phone` Nullable(String),
    `Store_Email_Address` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Workshop_Group_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Performers` (
    `Performer_ID` Int64,
    `Address_ID` Int64,
    `Customer_Name` Nullable(String),
    `Customer_Phone` Nullable(String),
    `Customer_Email_Address` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Performer_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Customers` (
    `Customer_ID` String,
    `Address_ID` Int64,
    `Customer_Name` Nullable(String),
    `Customer_Phone` Nullable(String),
    `Customer_Email_Address` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Customer_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Stores` (
    `Store_ID` String,
    `Address_ID` Int64,
    `Marketing_Region_Code` String,
    `Store_Name` Nullable(String),
    `Store_Phone` Nullable(String),
    `Store_Email_Address` Nullable(String),
    `Other_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Store_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Bookings` (
    `Booking_ID` Int64,
    `Customer_ID` Int64,
    `Workshop_Group_ID` String,
    `Status_Code` String,
    `Store_ID` Int64,
    `Order_Date` DateTime,
    `Planned_Delivery_Date` DateTime,
    `Actual_Delivery_Date` DateTime,
    `Other_Order_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Booking_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Performers_in_Bookings` (
    `Order_ID` Int64,
    `Performer_ID` Int64
)
ENGINE = MergeTree()
ORDER BY (`Order_ID`, `Performer_ID`);

CREATE TABLE `cre_Drama_Workshop_Groups`.`Customer_Orders` (
    `Order_ID` Int64,
    `Customer_ID` Int64,
    `Store_ID` Int64,
    `Order_Date` DateTime,
    `Planned_Delivery_Date` DateTime,
    `Actual_Delivery_Date` DateTime,
    `Other_Order_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Order_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Order_Items` (
    `Order_Item_ID` Int64,
    `Order_ID` Int64,
    `Product_ID` Int64,
    `Order_Quantity` Nullable(String),
    `Other_Item_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Order_Item_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Invoices` (
    `Invoice_ID` Int64,
    `Order_ID` Int64,
    `payment_method_code` Nullable(String),
    `Product_ID` Int64,
    `Order_Quantity` Nullable(String),
    `Other_Item_Details` Nullable(String),
    `Order_Item_ID` Int64
)
ENGINE = MergeTree()
ORDER BY `Invoice_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Services` (
    `Service_ID` Int64,
    `Service_Type_Code` Nullable(String),
    `Workshop_Group_ID` Int64,
    `Product_Description` Nullable(String),
    `Product_Name` Nullable(String),
    `Product_Price` Nullable(Decimal64(2)),
    `Other_Product_Service_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Service_ID`;

CREATE TABLE `cre_Drama_Workshop_Groups`.`Bookings_Services` (
    `Order_ID` Int64,
    `Product_ID` Int64
)
ENGINE = MergeTree()
ORDER BY (`Order_ID`, `Product_ID`);

CREATE TABLE `cre_Drama_Workshop_Groups`.`Invoice_Items` (
    `Invoice_Item_ID` Int64,
    `Invoice_ID` Int64,
    `Order_ID` Int64,
    `Order_Item_ID` Int64,
    `Product_ID` Int64,
    `Order_Quantity` Nullable(Int64),
    `Other_Item_Details` Nullable(String)
)
ENGINE = MergeTree()
ORDER BY `Invoice_Item_ID`;

