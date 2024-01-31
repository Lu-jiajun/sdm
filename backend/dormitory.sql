--
-- Create model CommApplicationModel
--
CREATE TABLE `comm_application` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `option` varchar(8) NOT NULL, `name` varchar(16) NOT NULL, `statu` varchar(16) NOT NULL, `approval_manager` varchar(16) NOT NULL);
--
-- Create model dormitory_management
--
CREATE TABLE `dormitory_management_info` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `building_number` varchar(255) NOT NULL);
--
-- Create model DormitoryInfoModel
--
CREATE TABLE `dormitory_info` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `building_number` varchar(255) NOT NULL, `dormitory_number` integer NOT NULL, `total_bed_number` integer NOT NULL, `empty_bed_number` integer NOT NULL, `head_of_dormitory` varchar(30) NOT NULL);
--
-- Create model ForeignerModel
--
CREATE TABLE `dormitory_foreigner` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `foreigner_name` varchar(255) NOT NULL, `inventory` integer NOT NULL, `dormitory_number` integer NOT NULL, `visit_datatime` datetime(6) NULL, `leave_datatime` datetime(6) NULL, `purpose` varchar(255) NOT NULL, `foreigner_phone_number` varchar(32) NULL);
--
-- Create model RepairApplicationModel
--
CREATE TABLE `repair_application` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `building_number` varchar(255) NOT NULL, `Student_ID` varchar(255) NOT NULL, `repair_title` varchar(30) NOT NULL);
--
-- Create model StudentInfoModel
--
CREATE TABLE `student_info` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `building_number` varchar(255) NOT NULL, `dormitory_number` integer NOT NULL, `bed_number` integer NOT NULL, `Student_ID` varchar(255) NOT NULL);
--
-- Create model StudentStatueModel
--
CREATE TABLE `student_statue_info` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `statue` varchar(8) NOT NULL, `Student_ID` varchar(255) NOT NULL);
