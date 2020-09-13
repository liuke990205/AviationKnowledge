/*
Navicat MySQL Data Transfer

Source Server         : Python
Source Server Version : 50648
Source Host           : localhost:3306
Source Database       : pymysql

Target Server Type    : MYSQL
Target Server Version : 50648
File Encoding         : 65001

Date: 2020-08-06 17:31:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add annotation', '7', 'add_annotation');
INSERT INTO `auth_permission` VALUES ('26', 'Can change annotation', '7', 'change_annotation');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete annotation', '7', 'delete_annotation');
INSERT INTO `auth_permission` VALUES ('28', 'Can view annotation', '7', 'view_annotation');
INSERT INTO `auth_permission` VALUES ('29', 'Can add dictionary', '8', 'add_dictionary');
INSERT INTO `auth_permission` VALUES ('30', 'Can change dictionary', '8', 'change_dictionary');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete dictionary', '8', 'delete_dictionary');
INSERT INTO `auth_permission` VALUES ('32', 'Can view dictionary', '8', 'view_dictionary');
INSERT INTO `auth_permission` VALUES ('33', 'Can add log', '9', 'add_log');
INSERT INTO `auth_permission` VALUES ('34', 'Can change log', '9', 'change_log');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete log', '9', 'delete_log');
INSERT INTO `auth_permission` VALUES ('36', 'Can view log', '9', 'view_log');
INSERT INTO `auth_permission` VALUES ('37', 'Can add relation', '10', 'add_relation');
INSERT INTO `auth_permission` VALUES ('38', 'Can change relation', '10', 'change_relation');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete relation', '10', 'delete_relation');
INSERT INTO `auth_permission` VALUES ('40', 'Can view relation', '10', 'view_relation');
INSERT INTO `auth_permission` VALUES ('41', 'Can add user', '11', 'add_user');
INSERT INTO `auth_permission` VALUES ('42', 'Can change user', '11', 'change_user');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete user', '11', 'delete_user');
INSERT INTO `auth_permission` VALUES ('44', 'Can view user', '11', 'view_user');
INSERT INTO `auth_permission` VALUES ('45', 'Can add temp', '12', 'add_temp');
INSERT INTO `auth_permission` VALUES ('46', 'Can change temp', '12', 'change_temp');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete temp', '12', 'delete_temp');
INSERT INTO `auth_permission` VALUES ('48', 'Can view temp', '12', 'view_temp');
INSERT INTO `auth_permission` VALUES ('49', 'Can add aircraft', '13', 'add_aircraft');
INSERT INTO `auth_permission` VALUES ('50', 'Can change aircraft', '13', 'change_aircraft');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete aircraft', '13', 'delete_aircraft');
INSERT INTO `auth_permission` VALUES ('52', 'Can view aircraft', '13', 'view_aircraft');
INSERT INTO `auth_permission` VALUES ('53', 'Can add model', '14', 'add_model');
INSERT INTO `auth_permission` VALUES ('54', 'Can change model', '14', 'change_model');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete model', '14', 'delete_model');
INSERT INTO `auth_permission` VALUES ('56', 'Can view model', '14', 'view_model');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('13', 'Hello', 'aircraft');
INSERT INTO `django_content_type` VALUES ('7', 'Hello', 'annotation');
INSERT INTO `django_content_type` VALUES ('8', 'Hello', 'dictionary');
INSERT INTO `django_content_type` VALUES ('9', 'Hello', 'log');
INSERT INTO `django_content_type` VALUES ('14', 'Hello', 'model');
INSERT INTO `django_content_type` VALUES ('10', 'Hello', 'relation');
INSERT INTO `django_content_type` VALUES ('12', 'Hello', 'temp');
INSERT INTO `django_content_type` VALUES ('11', 'Hello', 'user');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'Hello', '0001_initial', '2020-07-07 11:38:20.219494');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0001_initial', '2020-07-07 11:38:20.317775');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2020-07-07 11:38:20.480340');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0001_initial', '2020-07-07 11:38:20.820419');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0002_logentry_remove_auto_add', '2020-07-07 11:38:20.897176');
INSERT INTO `django_migrations` VALUES ('6', 'admin', '0003_logentry_add_action_flag_choices', '2020-07-07 11:38:20.908149');
INSERT INTO `django_migrations` VALUES ('7', 'contenttypes', '0002_remove_content_type_name', '2020-07-07 11:38:20.975965');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2020-07-07 11:38:21.028826');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2020-07-07 11:38:21.073704');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2020-07-07 11:38:21.084675');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2020-07-07 11:38:21.119582');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2020-07-07 11:38:21.126565');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2020-07-07 11:38:21.137534');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2020-07-07 11:38:21.181416');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0009_alter_user_last_name_max_length', '2020-07-07 11:38:21.225350');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0010_alter_group_name_max_length', '2020-07-07 11:38:21.271176');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0011_update_proxy_permissions', '2020-07-07 11:38:21.285144');
INSERT INTO `django_migrations` VALUES ('18', 'sessions', '0001_initial', '2020-07-07 11:38:21.313064');
INSERT INTO `django_migrations` VALUES ('19', 'Hello', '0002_auto_20200708_1225', '2020-07-08 04:25:12.657502');
INSERT INTO `django_migrations` VALUES ('20', 'Hello', '0003_aircraft_model', '2020-07-21 05:02:44.540064');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('3f5rb88u8svtdgtwhc3xez1tgs41ryf7', 'ODU2ZTYyMGY4NGFkNmI5MzdlNTY4YmJiZmNkZGI2ZmVhNTQwNGNlZTp7InVzZXJuYW1lIjoidGVzdDIiLCJlbnRpdHkxIjoiWFx1NTc4Ylx1OThkZVx1NjczYSIsInJlbGF0aW9uIjoiXHU1M2MyXHU4MDAzIiwiZW50aXR5MiI6IiIsImVudGl0eSI6IlhcdTU3OGJcdTk4ZGVcdTY3M2EifQ==', '2020-07-27 14:53:17.616299');
INSERT INTO `django_session` VALUES ('fxqn6yqo7s6wg3vnc4xqsidcvqbwz0j5', 'YjEyNmY3NTkzNTI3MzU2MjhlY2Q2MTRjNjFmZGU1YTkyY2Y4NjY3MTp7InVzZXJuYW1lIjoidGVzdCJ9', '2020-07-28 17:27:33.163887');
INSERT INTO `django_session` VALUES ('hvfqa22f89l3brf1uqgtca2s3z1xagfb', 'YjEyNmY3NTkzNTI3MzU2MjhlY2Q2MTRjNjFmZGU1YTkyY2Y4NjY3MTp7InVzZXJuYW1lIjoidGVzdCJ9', '2020-07-28 17:39:38.711076');
INSERT INTO `django_session` VALUES ('l0sf3atw0rl5yilocokex1x4z5cl8wj6', 'MDlkYTIyN2Y1MjVmMjMwZTFiODhmMDQyNDViODE2ZGM5YTYyOGJhZjp7InVzZXJuYW1lIjoidGVzdCIsImVudGl0eTEiOiJYXHU1NzhiXHU5OGRlXHU2NzNhIiwicmVsYXRpb24iOiIiLCJlbnRpdHkyIjoiIiwidGFibGUiOiJtb2RlbCIsInRhYmxlMiI6ImFpcmNyYWZ0IiwicmVfbmFtZSI6Im1vZGVsX25hbWUifQ==', '2020-08-20 09:30:26.719166');
INSERT INTO `django_session` VALUES ('zj9807vju7j2fa90lvl2y55b7os8m2iz', 'YjEyNmY3NTkzNTI3MzU2MjhlY2Q2MTRjNjFmZGU1YTkyY2Y4NjY3MTp7InVzZXJuYW1lIjoidGVzdCJ9', '2020-07-28 17:43:16.028754');

-- ----------------------------
-- Table structure for hello_aircraft
-- ----------------------------
DROP TABLE IF EXISTS `hello_aircraft`;
CREATE TABLE `hello_aircraft` (
  `aircraft_id` int(11) NOT NULL AUTO_INCREMENT,
  `aircraft_name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`aircraft_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_aircraft
-- ----------------------------
INSERT INTO `hello_aircraft` VALUES ('1', 'X型飞机', 'AA');

-- ----------------------------
-- Table structure for hello_annotation
-- ----------------------------
DROP TABLE IF EXISTS `hello_annotation`;
CREATE TABLE `hello_annotation` (
  `annotation_id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `flag` tinyint(1) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`annotation_id`),
  KEY `Hello_annotation_user_id_id_ad6732e5_fk_Hello_user_user_id` (`user_id_id`),
  CONSTRAINT `Hello_annotation_user_id_id_ad6732e5_fk_Hello_user_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `hello_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=248 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_annotation
-- ----------------------------
INSERT INTO `hello_annotation` VALUES ('38', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('39', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('40', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('41', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('42', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('43', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('44', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('45', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('46', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('47', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('48', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('49', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('50', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('51', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('52', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('53', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('54', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('55', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('56', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('57', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('58', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('59', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('60', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('61', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('62', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('63', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('64', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('65', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('66', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('67', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('68', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('69', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('70', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('71', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('72', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('73', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('74', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('75', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('76', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('77', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('78', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('79', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('80', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('81', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('82', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('83', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('84', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('85', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('86', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('87', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('88', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('89', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('90', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('91', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('92', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('93', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('94', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('95', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('96', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('97', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('98', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('99', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('100', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('101', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('102', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('103', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('104', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('105', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('106', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('107', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('108', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('109', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('110', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('111', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('112', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('113', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('114', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('115', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('116', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('117', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('118', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('119', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('120', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('121', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('122', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('123', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('124', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('125', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('126', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('127', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('128', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('129', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('130', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('131', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('132', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('133', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('134', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('135', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('136', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('137', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('138', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('139', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('140', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('141', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('142', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('143', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('144', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('145', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('146', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('147', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('148', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('149', '战斗机往往携带巡航导弹执行任务。', '1', 'data2.txt', '1');
INSERT INTO `hello_annotation` VALUES ('150', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('151', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('152', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('153', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('154', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('155', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('156', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('157', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('158', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('159', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('160', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('161', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('162', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('163', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('164', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('165', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('166', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('167', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('168', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('169', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('170', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('171', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('172', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('173', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('174', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('175', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('176', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('177', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('178', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('179', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('180', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('181', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('182', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('183', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('184', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('185', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('186', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('187', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('188', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('189', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('190', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('191', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('192', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('193', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('194', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('195', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('196', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('197', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('198', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('199', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('200', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('201', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('202', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('203', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('204', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('205', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('206', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('207', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('208', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('209', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('210', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('211', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('212', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('213', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('214', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('215', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('216', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('217', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('218', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('219', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('220', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '0', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('221', '战斗机往往携带巡航导弹执行任务。', '0', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('222', '战斗机的维修时间大约半个月左右。', '0', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('223', 'X型飞机的设计采用《IO868-P-90》标准。', '0', 'data.docx', '4');
INSERT INTO `hello_annotation` VALUES ('224', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('225', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('226', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('227', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('228', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('229', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('230', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('231', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('232', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('233', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('234', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('235', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('236', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('237', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('238', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('239', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('240', '战斗机的维修时间大约半个月左右。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('241', 'X型飞机的设计采用《IO868-P-90》标准。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('242', '在X型飞机的设计建模过程中，涉及到平尾承力布置数模、前机身承力构建布置数模、外形数模等多种数学模型。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('243', '其中，平尾承力布置数模的设计按照标准《18D-WXSM-B-121》执行。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('244', '保障系统是X型飞机的重要组成部分，其使用可用度应不小于0.9，维修时间应不大于2小时。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('245', '战斗机往往携带巡航导弹执行任务。', '1', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('246', '战斗机的维修时间大约半个月左右。', '0', 'data.docx', '1');
INSERT INTO `hello_annotation` VALUES ('247', 'X型飞机的设计采用《IO868-P-90》标准。', '0', 'data.docx', '1');

-- ----------------------------
-- Table structure for hello_dictionary
-- ----------------------------
DROP TABLE IF EXISTS `hello_dictionary`;
CREATE TABLE `hello_dictionary` (
  `dictionary_id` int(11) NOT NULL AUTO_INCREMENT,
  `entity` varchar(100) NOT NULL,
  `entity_type` varchar(100) NOT NULL,
  PRIMARY KEY (`dictionary_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_dictionary
-- ----------------------------
INSERT INTO `hello_dictionary` VALUES ('1', 'X型飞机', '航空器');
INSERT INTO `hello_dictionary` VALUES ('2', '战斗机', '航空器');
INSERT INTO `hello_dictionary` VALUES ('3', '巡航导弹', '武器');
INSERT INTO `hello_dictionary` VALUES ('4', '保障系统', '系统');
INSERT INTO `hello_dictionary` VALUES ('5', '平尾承力布置数模', '数学模型');
INSERT INTO `hello_dictionary` VALUES ('6', '前机身承力构建布置数模', '数学模型');
INSERT INTO `hello_dictionary` VALUES ('7', '外形数模', '数学模型');
INSERT INTO `hello_dictionary` VALUES ('8', '使用可用度', '性能指标');
INSERT INTO `hello_dictionary` VALUES ('9', '维修时间', '性能指标');
INSERT INTO `hello_dictionary` VALUES ('10', '再次出动时间', '性能指标');
INSERT INTO `hello_dictionary` VALUES ('11', '18D-WXSM-B-121', '参考文档');
INSERT INTO `hello_dictionary` VALUES ('12', 'IO868-P-90', '参考文档');
INSERT INTO `hello_dictionary` VALUES ('13', 'Y型飞机', '航空器');
INSERT INTO `hello_dictionary` VALUES ('14', 'Z型飞机', '航空器');
INSERT INTO `hello_dictionary` VALUES ('15', '波音747', '航空器');

-- ----------------------------
-- Table structure for hello_log
-- ----------------------------
DROP TABLE IF EXISTS `hello_log`;
CREATE TABLE `hello_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `annotation_id` varchar(10) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_log
-- ----------------------------
INSERT INTO `hello_log` VALUES ('1', '245', '1');
INSERT INTO `hello_log` VALUES ('2', '5', '3');
INSERT INTO `hello_log` VALUES ('3', '219', '4');

-- ----------------------------
-- Table structure for hello_model
-- ----------------------------
DROP TABLE IF EXISTS `hello_model`;
CREATE TABLE `hello_model` (
  `model_id` int(11) NOT NULL AUTO_INCREMENT,
  `model_name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`model_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_model
-- ----------------------------

-- ----------------------------
-- Table structure for hello_relation
-- ----------------------------
DROP TABLE IF EXISTS `hello_relation`;
CREATE TABLE `hello_relation` (
  `relation_id` int(11) NOT NULL AUTO_INCREMENT,
  `head_entity` varchar(100) NOT NULL,
  `tail_entity` varchar(100) NOT NULL,
  `relation` varchar(100) NOT NULL,
  PRIMARY KEY (`relation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_relation
-- ----------------------------
INSERT INTO `hello_relation` VALUES ('1', '航空器', '航空器', '上下位');
INSERT INTO `hello_relation` VALUES ('2', '航空器', '武器', '使用');
INSERT INTO `hello_relation` VALUES ('3', '航空器', '系统', '组成');
INSERT INTO `hello_relation` VALUES ('4', '航空器', '数学模型', '参考');
INSERT INTO `hello_relation` VALUES ('5', '数学模型', '参考文档', '参考');
INSERT INTO `hello_relation` VALUES ('6', '航空器', '性能指标', '性能指标');
INSERT INTO `hello_relation` VALUES ('7', '性能指标', '参数值', '性能指标');
INSERT INTO `hello_relation` VALUES ('8', '人物', '身高', '属于');
INSERT INTO `hello_relation` VALUES ('9', '航空器', '参考文档', '参考');

-- ----------------------------
-- Table structure for hello_temp
-- ----------------------------
DROP TABLE IF EXISTS `hello_temp`;
CREATE TABLE `hello_temp` (
  `temp_id` int(11) NOT NULL AUTO_INCREMENT,
  `headEntity` varchar(100) NOT NULL,
  `headEntityType` varchar(100) NOT NULL,
  `tailEntity` varchar(100) NOT NULL,
  `tailEntityType` varchar(100) NOT NULL,
  `relationshipCategory` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `annotation_id_id` int(11) NOT NULL,
  PRIMARY KEY (`temp_id`),
  KEY `Hello_temp_annotation_id_id_86881eb9_fk_Hello_ann` (`annotation_id_id`),
  CONSTRAINT `Hello_temp_annotation_id_id_86881eb9_fk_Hello_ann` FOREIGN KEY (`annotation_id_id`) REFERENCES `hello_annotation` (`annotation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=489 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_temp
-- ----------------------------
INSERT INTO `hello_temp` VALUES ('402', 'X型飞机', '航空器', '平尾承力布置数模', '数学模型', '参考', '4', 'data.docx', '188');
INSERT INTO `hello_temp` VALUES ('403', 'X型飞机', '航空器', '前机身承力构建布置数模', '数学模型', '参考', '4', 'data.docx', '188');
INSERT INTO `hello_temp` VALUES ('404', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '4', 'data.docx', '188');
INSERT INTO `hello_temp` VALUES ('405', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '189');
INSERT INTO `hello_temp` VALUES ('407', 'X型飞机', '航空器', '使用可用度', '性能指标', '性能指标', '4', 'data.docx', '190');
INSERT INTO `hello_temp` VALUES ('408', 'X型飞机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '190');
INSERT INTO `hello_temp` VALUES ('409', '战斗机', '航空器', '巡航导弹', '武器', '使用', '4', 'data.docx', '191');
INSERT INTO `hello_temp` VALUES ('412', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '195');
INSERT INTO `hello_temp` VALUES ('413', '战斗机', '航空器', '巡航导弹', '武器', '使用', '4', 'data.docx', '197');
INSERT INTO `hello_temp` VALUES ('414', '战斗机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '198');
INSERT INTO `hello_temp` VALUES ('415', 'X型飞机', '航空器', 'IO868-P-90', '参考文档', '参考', '4', 'data.docx', '199');
INSERT INTO `hello_temp` VALUES ('417', 'X型飞机', '航空器', '前机身承力构建布置数模', '数学模型', '参考', '4', 'data.docx', '200');
INSERT INTO `hello_temp` VALUES ('418', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '4', 'data.docx', '200');
INSERT INTO `hello_temp` VALUES ('419', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '201');
INSERT INTO `hello_temp` VALUES ('420', '战斗机', '武器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '201');
INSERT INTO `hello_temp` VALUES ('421', 'X型飞机', '航空器', '保障系统', '系统', '组成', '4', 'data.docx', '202');
INSERT INTO `hello_temp` VALUES ('422', 'X型飞机', '航空器', '使用可用度', '性能指标', '性能指标', '4', 'data.docx', '202');
INSERT INTO `hello_temp` VALUES ('423', 'X型飞机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '202');
INSERT INTO `hello_temp` VALUES ('424', '战斗机', '航空器', '巡航导弹', '武器', '使用', '4', 'data.docx', '203');
INSERT INTO `hello_temp` VALUES ('425', '战斗机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '204');
INSERT INTO `hello_temp` VALUES ('426', 'X型飞机', '航空器', '平尾承力布置数模', '数学模型', '参考', '4', 'data.docx', '206');
INSERT INTO `hello_temp` VALUES ('427', 'X型飞机', '航空器', '前机身承力构建布置数模', '数学模型', '参考', '4', 'data.docx', '206');
INSERT INTO `hello_temp` VALUES ('428', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '4', 'data.docx', '206');
INSERT INTO `hello_temp` VALUES ('429', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '207');
INSERT INTO `hello_temp` VALUES ('430', 'X型飞机', '航空器', '保障系统', '系统', '组成', '4', 'data.docx', '208');
INSERT INTO `hello_temp` VALUES ('431', 'X型飞机', '航空器', '使用可用度', '性能指标', '性能指标', '4', 'data.docx', '208');
INSERT INTO `hello_temp` VALUES ('432', 'X型飞机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '208');
INSERT INTO `hello_temp` VALUES ('433', '战斗机', '航空器', '巡航导弹', '武器', '使用', '4', 'data.docx', '209');
INSERT INTO `hello_temp` VALUES ('434', '战斗机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '210');
INSERT INTO `hello_temp` VALUES ('435', 'X型飞机', '航空器', 'IO868-P-90', '参考文档', '参考', '4', 'data.docx', '211');
INSERT INTO `hello_temp` VALUES ('436', 'X型飞机', '航空器', '平尾承力布置数模', '数学模型', '参考', '4', 'data.docx', '212');
INSERT INTO `hello_temp` VALUES ('437', 'X型飞机', '航空器', '前机身承力构建布置数模', '数学模型', '参考', '4', 'data.docx', '212');
INSERT INTO `hello_temp` VALUES ('438', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '4', 'data.docx', '212');
INSERT INTO `hello_temp` VALUES ('439', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '213');
INSERT INTO `hello_temp` VALUES ('440', 'X型飞机', '航空器', '保障系统', '系统', '组成', '4', 'data.docx', '214');
INSERT INTO `hello_temp` VALUES ('441', 'X型飞机', '航空器', '使用可用度', '性能指标', '性能指标', '4', 'data.docx', '214');
INSERT INTO `hello_temp` VALUES ('442', 'X型飞机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '214');
INSERT INTO `hello_temp` VALUES ('443', '战斗机', '航空器', '维修时间', '性能指标', '性能指标', '4', 'data.docx', '216');
INSERT INTO `hello_temp` VALUES ('444', 'X型飞机', '航空器', 'IO868-P-90', '参考文档', '参考', '4', 'data.docx', '217');
INSERT INTO `hello_temp` VALUES ('445', 'X型飞机', '航空器', '平尾承力布置数模', '数学模型', '参考', '4', 'data.docx', '218');
INSERT INTO `hello_temp` VALUES ('446', 'X型飞机', '航空器', '前机身承力构建布置数模', '数学模型', '参考', '4', 'data.docx', '218');
INSERT INTO `hello_temp` VALUES ('447', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '4', 'data.docx', '218');
INSERT INTO `hello_temp` VALUES ('448', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '4', 'data.docx', '219');
INSERT INTO `hello_temp` VALUES ('483', 'X型飞机', '航空器', '外形数模', '数学模型', '参考', '1', 'data.docx', '242');
INSERT INTO `hello_temp` VALUES ('484', '平尾承力布置数模', '数学模型', '18D-WXSM-B-121', '参考文档', '参考', '1', 'data.docx', '243');
INSERT INTO `hello_temp` VALUES ('485', 'X型飞机', '航空器', '保障系统', '系统', '组成', '1', 'data.docx', '244');
INSERT INTO `hello_temp` VALUES ('486', 'X型飞机', '航空器', '使用可用度', '性能指标', '性能指标', '1', 'data.docx', '244');
INSERT INTO `hello_temp` VALUES ('487', 'X型飞机', '航空器', '维修时间', '性能指标', '性能指标', '1', 'data.docx', '244');
INSERT INTO `hello_temp` VALUES ('488', '战斗机', '航空器', '巡航导弹', '武器', '使用', '1', 'data.docx', '245');

-- ----------------------------
-- Table structure for hello_user
-- ----------------------------
DROP TABLE IF EXISTS `hello_user`;
CREATE TABLE `hello_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hello_user
-- ----------------------------
INSERT INTO `hello_user` VALUES ('1', 'test', 'test');
INSERT INTO `hello_user` VALUES ('3', 'liuke', 'test');
INSERT INTO `hello_user` VALUES ('4', 'test2', 'test2');
