--
-- Create model CrudDemoModel
--
CREATE TABLE `goods` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NULL, `modifier` varchar(255) NULL, `dept_belong_id` varchar(255) NULL, `update_datetime` datetime(6) NULL, `create_datetime` datetime(6) NULL, `goods` varchar(255) NOT NULL, `inventory` integer NOT NULL, `goods_price` double precision NOT NULL, `purchase_goods_date` date NOT NULL);
