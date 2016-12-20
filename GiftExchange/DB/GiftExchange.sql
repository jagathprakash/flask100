-- Adminer 4.2.5 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `Participants`;
CREATE TABLE `Participants` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `address` tinytext NOT NULL,
  `gifts` tinytext NOT NULL,
  `charity` tinytext NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2016-12-20 16:13:09
