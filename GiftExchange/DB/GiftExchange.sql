-- Adminer 4.2.5 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `GiftExchange`;
CREATE DATABASE `GiftExchange` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `GiftExchange`;

DROP TABLE IF EXISTS `participants`;
CREATE TABLE `participants` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `address` tinytext NOT NULL,
  `gifts` tinytext NOT NULL,
  `charity` tinytext NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2016-12-22 17:24:15
