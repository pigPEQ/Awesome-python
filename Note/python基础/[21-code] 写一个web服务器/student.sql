/*
 Navicat Premium Data Transfer

 Source Server         : hello mysql
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : python

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 17/03/2021 23:57:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `age` tinyint DEFAULT NULL,
  `sex` enum('男','女') DEFAULT '男',
  `t_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES (1, '张三', 21, '男', 1);
INSERT INTO `student` VALUES (2, '李四', 23, '女', 2);
INSERT INTO `student` VALUES (4, '王五', 19, '男', NULL);
INSERT INTO `student` VALUES (5, '张杰', 23, '男', NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
