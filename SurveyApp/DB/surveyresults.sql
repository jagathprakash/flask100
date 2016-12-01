-- Adminer 4.2.5 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';

DROP DATABASE IF EXISTS `ArchiveSurvey`;
CREATE DATABASE `ArchiveSurvey` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `ArchiveSurvey`;

DROP TABLE IF EXISTS `surveyresults`;
CREATE TABLE `surveyresults` (
  `surveyid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `slack` varchar(10) NOT NULL,
  `choice1` tinyint(1) NOT NULL,
  `choice2` tinyint(1) NOT NULL,
  `choice3` tinyint(1) NOT NULL,
  `choice4` tinyint(1) NOT NULL,
  `general` longtext,
  PRIMARY KEY (`surveyid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2016-11-30 16:05:00
