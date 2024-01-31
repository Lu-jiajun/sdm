--
-- Create model Users
--
CREATE TABLE `dvadmin_system_users` (`password` varchar(128) NOT NULL, `last_login` datetime(6) NULL, `is_superuser` bool NOT NULL, `first_name` varchar(150) NOT NULL, `last_name` varchar(150) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime(6) NOT NULL, `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `username` varchar(150) NOT NULL UNIQUE, `employee_no` varchar(150) NULL UNIQUE, `email` varchar(255) NULL, `mobile` varchar(255) NULL, `avatar` varchar(255) NULL, `name` varchar(40) NOT NULL, `gender` integer NULL, `user_type` integer NULL, `last_token` varchar(255) NULL, `creator_id` bigint NULL);
--
-- Create model Dept
--
CREATE TABLE `dvadmin_system_dept` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(64) NOT NULL, `key` varchar(64) NULL UNIQUE, `sort` integer NOT NULL, `owner` varchar(32) NULL, `phone` varchar(32) NULL, `email` varchar(32) NULL, `status` bool NULL, `creator_id` bigint NULL, `parent_id` bigint NULL);
--
-- Create model Menu
--
CREATE TABLE `dvadmin_system_menu` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `icon` varchar(64) NULL, `name` varchar(64) NOT NULL, `sort` integer NULL, `is_link` bool NOT NULL, `is_catalog` bool NOT NULL, `web_path` varchar(128) NULL, `component` varchar(128) NULL, `component_name` varchar(50) NULL, `status` bool NOT NULL, `frame_out` bool NOT NULL, `cache` bool NOT NULL, `visible` bool NOT NULL, `creator_id` bigint NULL, `parent_id` bigint NULL);
--
-- Create model MenuButton
--
CREATE TABLE `dvadmin_system_menu_button` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(64) NOT NULL, `value` varchar(64) NOT NULL, `api` varchar(200) NOT NULL, `method` integer NULL, `creator_id` bigint NULL, `menu_id` bigint NOT NULL);
--
-- Create model MessageCenter
--
CREATE TABLE `dvadmin_message_center` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `title` varchar(100) NOT NULL, `content` longtext NOT NULL, `target_type` integer NOT NULL, `creator_id` bigint NULL);
CREATE TABLE `dvadmin_message_center_target_dept` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `messagecenter_id` bigint NOT NULL, `dept_id` bigint NOT NULL);
--
-- Create model Role
--
CREATE TABLE `dvadmin_system_role` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(64) NOT NULL, `key` varchar(64) NOT NULL UNIQUE, `sort` integer NOT NULL, `status` bool NOT NULL, `admin` bool NOT NULL, `data_range` integer NOT NULL, `remark` longtext NULL, `creator_id` bigint NULL);
CREATE TABLE `dvadmin_system_role_dept` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `role_id` bigint NOT NULL, `dept_id` bigint NOT NULL);
CREATE TABLE `dvadmin_system_role_menu` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `role_id` bigint NOT NULL, `menu_id` bigint NOT NULL);
CREATE TABLE `dvadmin_system_role_permission` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `role_id` bigint NOT NULL, `menubutton_id` bigint NOT NULL);
--
-- Create model Post
--
CREATE TABLE `dvadmin_system_post` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(64) NOT NULL, `code` varchar(32) NOT NULL, `sort` integer NOT NULL, `status` integer NOT NULL, `creator_id` bigint NULL);
--
-- Create model OperationLog
--
CREATE TABLE `dvadmin_system_operation_log` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `request_modular` varchar(64) NULL, `request_path` varchar(400) NULL, `request_body` longtext NULL, `request_method` varchar(8) NULL, `request_msg` longtext NULL, `request_ip` varchar(32) NULL, `request_browser` varchar(64) NULL, `response_code` varchar(32) NULL, `request_os` varchar(64) NULL, `json_result` longtext NULL, `status` bool NOT NULL, `creator_id` bigint NULL);
--
-- Create model MessageCenterTargetUser
--
CREATE TABLE `dvadmin_message_center_target_user` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `is_read` bool NULL, `creator_id` bigint NULL, `messagecenter_id` bigint NOT NULL, `users_id` bigint NOT NULL);
--
-- Add field target_role to messagecenter
--
CREATE TABLE `dvadmin_message_center_target_role` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `messagecenter_id` bigint NOT NULL, `role_id` bigint NOT NULL);
--
-- Add field target_user to messagecenter
--
--
-- Create model LoginLog
--
CREATE TABLE `dvadmin_system_login_log` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `username` varchar(150) NULL, `ip` varchar(32) NULL, `agent` longtext NULL, `browser` varchar(200) NULL, `os` varchar(200) NULL, `continent` varchar(50) NULL, `country` varchar(50) NULL, `province` varchar(50) NULL, `city` varchar(50) NULL, `district` varchar(50) NULL, `isp` varchar(50) NULL, `area_code` varchar(50) NULL, `country_english` varchar(50) NULL, `country_code` varchar(50) NULL, `longitude` varchar(50) NULL, `latitude` varchar(50) NULL, `login_type` integer NOT NULL, `creator_id` bigint NULL);
--
-- Create model FileList
--
CREATE TABLE `dvadmin_system_file_list` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(200) NULL, `url` varchar(100) NULL, `file_url` varchar(255) NOT NULL, `engine` varchar(100) NOT NULL, `mime_type` varchar(100) NOT NULL, `size` bigint NOT NULL, `md5sum` varchar(36) NOT NULL, `creator_id` bigint NULL);
--
-- Create model Dictionary
--
CREATE TABLE `dvadmin_system_dictionary` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `label` varchar(100) NULL, `value` varchar(200) NULL, `type` integer NOT NULL, `color` varchar(20) NULL, `is_value` bool NOT NULL, `status` bool NOT NULL, `sort` integer NULL, `remark` varchar(2000) NULL, `creator_id` bigint NULL, `parent_id` bigint NULL);
--
-- Create model Area
--
CREATE TABLE `dvadmin_system_area` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `name` varchar(100) NOT NULL, `code` varchar(20) NOT NULL UNIQUE, `level` bigint NOT NULL, `pinyin` varchar(255) NOT NULL, `initials` varchar(20) NOT NULL, `enable` bool NOT NULL, `creator_id` bigint NULL, `pcode_id` varchar(20) NULL);
--
-- Create model ApiWhiteList
--
CREATE TABLE `dvadmin_api_white_list` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `url` varchar(200) NOT NULL, `method` integer NULL, `enable_datasource` bool NOT NULL, `creator_id` bigint NULL);
--
-- Add field dept to users
--
ALTER TABLE `dvadmin_system_users` ADD COLUMN `dept_id` bigint NULL;
--
-- Add field groups to users
--
CREATE TABLE `dvadmin_system_users_groups` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `users_id` bigint NOT NULL, `group_id` integer NOT NULL);
--
-- Add field post to users
--
CREATE TABLE `dvadmin_system_users_post` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `users_id` bigint NOT NULL, `post_id` bigint NOT NULL);
--
-- Add field role to users
--
CREATE TABLE `dvadmin_system_users_role` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `users_id` bigint NOT NULL, `role_id` bigint NOT NULL);
--
-- Add field user_permissions to users
--
CREATE TABLE `dvadmin_system_users_user_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `users_id` bigint NOT NULL, `permission_id` integer NOT NULL);
--
-- Create model SystemConfig
--
CREATE TABLE `dvadmin_system_config` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `title` varchar(50) NOT NULL, `key` varchar(200) NOT NULL, `value` json NULL, `sort` integer NOT NULL, `status` bool NOT NULL, `data_options` json NULL, `form_item_type` integer NOT NULL, `rule` json NULL, `placeholder` varchar(100) NULL, `setting` json NULL, `creator_id` bigint NULL, `parent_id` bigint NULL);
CREATE INDEX `dvadmin_system_users_creator_id_28556713` ON `dvadmin_system_users` (`creator_id`);
CREATE INDEX `dvadmin_system_dept_creator_id_e69fd1ae` ON `dvadmin_system_dept` (`creator_id`);
CREATE INDEX `dvadmin_system_dept_parent_id_0f9eb419` ON `dvadmin_system_dept` (`parent_id`);
CREATE INDEX `dvadmin_system_menu_creator_id_430cdc1c` ON `dvadmin_system_menu` (`creator_id`);
CREATE INDEX `dvadmin_system_menu_parent_id_bc6f21bc` ON `dvadmin_system_menu` (`parent_id`);
CREATE INDEX `dvadmin_system_menu_button_creator_id_3df058f7` ON `dvadmin_system_menu_button` (`creator_id`);
CREATE INDEX `dvadmin_system_menu_button_menu_id_f6aafcd8` ON `dvadmin_system_menu_button` (`menu_id`);
CREATE INDEX `dvadmin_message_center_creator_id_60e2080e` ON `dvadmin_message_center` (`creator_id`);
ALTER TABLE `dvadmin_message_center_target_dept` ADD CONSTRAINT `dvadmin_message_center_t_messagecenter_id_dept_id_d9fb0c77_uniq` UNIQUE (`messagecenter_id`, `dept_id`);
CREATE INDEX `dvadmin_message_center_target_dept_messagecenter_id_69868c17` ON `dvadmin_message_center_target_dept` (`messagecenter_id`);
CREATE INDEX `dvadmin_message_center_target_dept_dept_id_616decc4` ON `dvadmin_message_center_target_dept` (`dept_id`);
CREATE INDEX `dvadmin_system_role_creator_id_a89a9bc7` ON `dvadmin_system_role` (`creator_id`);
ALTER TABLE `dvadmin_system_role_dept` ADD CONSTRAINT `dvadmin_system_role_dept_role_id_dept_id_524d7fba_uniq` UNIQUE (`role_id`, `dept_id`);
CREATE INDEX `dvadmin_system_role_dept_role_id_4f737c95` ON `dvadmin_system_role_dept` (`role_id`);
CREATE INDEX `dvadmin_system_role_dept_dept_id_d719761c` ON `dvadmin_system_role_dept` (`dept_id`);
ALTER TABLE `dvadmin_system_role_menu` ADD CONSTRAINT `dvadmin_system_role_menu_role_id_menu_id_06192289_uniq` UNIQUE (`role_id`, `menu_id`);
CREATE INDEX `dvadmin_system_role_menu_role_id_dcc80258` ON `dvadmin_system_role_menu` (`role_id`);
CREATE INDEX `dvadmin_system_role_menu_menu_id_7bbf1cb9` ON `dvadmin_system_role_menu` (`menu_id`);
ALTER TABLE `dvadmin_system_role_permission` ADD CONSTRAINT `dvadmin_system_role_perm_role_id_menubutton_id_46c1e3ca_uniq` UNIQUE (`role_id`, `menubutton_id`);
CREATE INDEX `dvadmin_system_role_permission_role_id_bf988ad5` ON `dvadmin_system_role_permission` (`role_id`);
CREATE INDEX `dvadmin_system_role_permission_menubutton_id_7ba32ee0` ON `dvadmin_system_role_permission` (`menubutton_id`);
CREATE INDEX `dvadmin_system_post_creator_id_b5ef9351` ON `dvadmin_system_post` (`creator_id`);
CREATE INDEX `dvadmin_system_operation_log_creator_id_0914479c` ON `dvadmin_system_operation_log` (`creator_id`);
CREATE INDEX `dvadmin_message_center_target_user_creator_id_0a27a561` ON `dvadmin_message_center_target_user` (`creator_id`);
CREATE INDEX `dvadmin_message_center_target_user_messagecenter_id_54f35bf8` ON `dvadmin_message_center_target_user` (`messagecenter_id`);
CREATE INDEX `dvadmin_message_center_target_user_users_id_9ff81ff5` ON `dvadmin_message_center_target_user` (`users_id`);
ALTER TABLE `dvadmin_message_center_target_role` ADD CONSTRAINT `dvadmin_message_center_t_messagecenter_id_role_id_f5a77970_uniq` UNIQUE (`messagecenter_id`, `role_id`);
CREATE INDEX `dvadmin_message_center_target_role_messagecenter_id_41a7bd9d` ON `dvadmin_message_center_target_role` (`messagecenter_id`);
CREATE INDEX `dvadmin_message_center_target_role_role_id_661a61bb` ON `dvadmin_message_center_target_role` (`role_id`);
CREATE INDEX `dvadmin_system_login_log_creator_id_5f6dc165` ON `dvadmin_system_login_log` (`creator_id`);
CREATE INDEX `dvadmin_system_file_list_creator_id_dec6acb5` ON `dvadmin_system_file_list` (`creator_id`);
CREATE INDEX `dvadmin_system_dictionary_creator_id_d1b44b9d` ON `dvadmin_system_dictionary` (`creator_id`);
CREATE INDEX `dvadmin_system_dictionary_parent_id_4cceb110` ON `dvadmin_system_dictionary` (`parent_id`);
CREATE INDEX `dvadmin_system_area_creator_id_a5046ac0` ON `dvadmin_system_area` (`creator_id`);
CREATE INDEX `dvadmin_system_area_pcode_id_f9b21462` ON `dvadmin_system_area` (`pcode_id`);
CREATE INDEX `dvadmin_api_white_list_creator_id_fd335789` ON `dvadmin_api_white_list` (`creator_id`);
CREATE INDEX `dvadmin_system_users_dept_id_b56f71f6` ON `dvadmin_system_users` (`dept_id`);
ALTER TABLE `dvadmin_system_users_groups` ADD CONSTRAINT `dvadmin_system_users_groups_users_id_group_id_7460f482_uniq` UNIQUE (`users_id`, `group_id`);
ALTER TABLE `dvadmin_system_users_groups` ADD CONSTRAINT `dvadmin_system_users_users_id_f20fa5bc_fk_dvadmin_s` FOREIGN KEY (`users_id`) REFERENCES `dvadmin_system_users` (`id`);
ALTER TABLE `dvadmin_system_users_groups` ADD CONSTRAINT `dvadmin_system_users_groups_group_id_42e8a6dc_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `dvadmin_system_users_post` ADD CONSTRAINT `dvadmin_system_users_post_users_id_post_id_41f83b22_uniq` UNIQUE (`users_id`, `post_id`);
CREATE INDEX `dvadmin_system_users_post_users_id_8ab2e760` ON `dvadmin_system_users_post` (`users_id`);
CREATE INDEX `dvadmin_system_users_post_post_id_50054985` ON `dvadmin_system_users_post` (`post_id`);
ALTER TABLE `dvadmin_system_users_role` ADD CONSTRAINT `dvadmin_system_users_role_users_id_role_id_02908e92_uniq` UNIQUE (`users_id`, `role_id`);
CREATE INDEX `dvadmin_system_users_role_users_id_a25207bc` ON `dvadmin_system_users_role` (`users_id`);
CREATE INDEX `dvadmin_system_users_role_role_id_e37d9591` ON `dvadmin_system_users_role` (`role_id`);
ALTER TABLE `dvadmin_system_users_user_permissions` ADD CONSTRAINT `dvadmin_system_users_use_users_id_permission_id_24cd72ef_uniq` UNIQUE (`users_id`, `permission_id`);
ALTER TABLE `dvadmin_system_users_user_permissions` ADD CONSTRAINT `dvadmin_system_users_users_id_fd3b0217_fk_dvadmin_s` FOREIGN KEY (`users_id`) REFERENCES `dvadmin_system_users` (`id`);
ALTER TABLE `dvadmin_system_users_user_permissions` ADD CONSTRAINT `dvadmin_system_users_permission_id_c8ec58dc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
ALTER TABLE `dvadmin_system_config` ADD CONSTRAINT `dvadmin_system_config_key_parent_id_f8627867_uniq` UNIQUE (`key`, `parent_id`);
CREATE INDEX `dvadmin_system_config_key_473a4f8d` ON `dvadmin_system_config` (`key`);
CREATE INDEX `dvadmin_system_config_creator_id_ba7fd60a` ON `dvadmin_system_config` (`creator_id`);
CREATE INDEX `dvadmin_system_config_parent_id_1ff841b5` ON `dvadmin_system_config` (`parent_id`);
