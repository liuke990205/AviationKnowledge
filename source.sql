/*
Navicat MySQL Data Transfer

Source Server         : Python
Source Server Version : 50648
Source Host           : localhost:3306
Source Database       : source

Target Server Type    : MYSQL
Target Server Version : 50648
File Encoding         : 65001

Date: 2020-08-06 17:31:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for aircraft
-- ----------------------------
DROP TABLE IF EXISTS `aircraft`;
CREATE TABLE `aircraft` (
  `aircraft_name` varchar(50) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `wight` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `model_name` varchar(50) DEFAULT NULL,
  `reference_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`aircraft_name`),
  KEY `model_name` (`model_name`),
  KEY `reference_name` (`reference_name`),
  CONSTRAINT `model_name` FOREIGN KEY (`model_name`) REFERENCES `model` (`model_name`),
  CONSTRAINT `reference_name` FOREIGN KEY (`reference_name`) REFERENCES `reference_file` (`reference_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of aircraft
-- ----------------------------
INSERT INTO `aircraft` VALUES ('X型飞机', '5', '9800', 'AA', '平尾承力布置数模', '18D-WXSM-B-121');
INSERT INTO `aircraft` VALUES ('Y型飞机', '3', '8699', 'BB', '外形数模', 'IO868-P-90');

-- ----------------------------
-- Table structure for model
-- ----------------------------
DROP TABLE IF EXISTS `model`;
CREATE TABLE `model` (
  `model_name` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `a` varchar(255) DEFAULT NULL,
  `b` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`model_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of model
-- ----------------------------
INSERT INTO `model` VALUES ('外形数模', 'AA', 'BB', 'CC');
INSERT INTO `model` VALUES ('平尾承力布置数模', 'CC', 'DD', 'GG');

-- ----------------------------
-- Table structure for reference_file
-- ----------------------------
DROP TABLE IF EXISTS `reference_file`;
CREATE TABLE `reference_file` (
  `reference_name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`reference_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of reference_file
-- ----------------------------
INSERT INTO `reference_file` VALUES ('18D-WXSM-B-121', 'EE');
INSERT INTO `reference_file` VALUES ('IO868-P-90', 'DD');
