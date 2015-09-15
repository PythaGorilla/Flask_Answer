-- --------------------------------------------------------
-- 主机:                           localhost
-- 服务器版本:                        5.7.7-rc-log - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 flask 的数据库结构
CREATE DATABASE IF NOT EXISTS `flask` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `flask`;


-- 导出  表 flask.context_table 结构
CREATE TABLE IF NOT EXISTS `context_table` (
  `uid` char(50) DEFAULT NULL,
  `cid` char(50) DEFAULT NULL,
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  flask.context_table 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `context_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `context_table` ENABLE KEYS */;


-- 导出  表 flask.conv_qa 结构
CREATE TABLE IF NOT EXISTS `conv_qa` (
  `qid` char(50) DEFAULT NULL,
  `transition_text` char(50) DEFAULT NULL,
  `choices` char(50) DEFAULT NULL,
  `context` char(50) DEFAULT NULL,
  `choice_type` char(50) DEFAULT NULL,
  `theme` char(50) DEFAULT NULL,
  `question` char(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  flask.conv_qa 的数据：~3 rows (大约)
/*!40000 ALTER TABLE `conv_qa` DISABLE KEYS */;
INSERT IGNORE INTO `conv_qa` (`qid`, `transition_text`, `choices`, `context`, `choice_type`, `theme`, `question`) VALUES
	('101', 'Let\'s talk together to select something to eat', '1-Yes:2-No\r\n', '1', 'choice', '1', 'Do you like meat?'),
	('102', 'OK', '1-Yes:2-No\r\n', '1', 'choice', '1', 'Do you like beef?'),
	('115', 'We have nothing more to serve', '1-Yes:2-No\r\n', '1', 'end', '1', 'That\'s it'),
	('103', 'OK', '1-Yes:2-No\r\n', '1', 'end', '1', 'We will prepare some beef KongPao');
/*!40000 ALTER TABLE `conv_qa` ENABLE KEYS */;


-- 导出  表 flask.state_table 结构
CREATE TABLE IF NOT EXISTS `state_table` (
  `uid` char(50) DEFAULT NULL,
  `cur` char(50) DEFAULT NULL,
  `prev` char(50) DEFAULT NULL,
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  flask.state_table 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `state_table` DISABLE KEYS */;
INSERT IGNORE INTO `state_table` (`uid`, `cur`, `prev`) VALUES
	('1', '115', '102'),
	('2', '101', '101');
/*!40000 ALTER TABLE `state_table` ENABLE KEYS */;


-- 导出  表 flask.user_conv_log 结构
CREATE TABLE IF NOT EXISTS `user_conv_log` (
  `uid` char(50) DEFAULT NULL,
  `qid` char(50) DEFAULT NULL,
  `choice` char(50) DEFAULT NULL,
  UNIQUE KEY `qid` (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  flask.user_conv_log 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `user_conv_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_conv_log` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
