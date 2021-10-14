-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Szerver verzió:               10.5.12-MariaDB - mariadb.org binary distribution
-- Szerver OS:                   Win64
-- HeidiSQL Verzió:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Struktúra mentése tábla fuzzyfta. elements
DROP TABLE IF EXISTS `elements`;
CREATE TABLE IF NOT EXISTS `elements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL DEFAULT 1,
  `event_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `event_id` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Tábla adatainak mentése fuzzyfta.elements: ~4 rows (hozzávetőleg)
DELETE FROM `elements`;
/*!40000 ALTER TABLE `elements` DISABLE KEYS */;
INSERT INTO `elements` (`id`, `level`, `event_id`) VALUES
	(1, 1, 1),
	(2, 1, 3),
	(3, 1, 2),
	(4, 1, 2);
/*!40000 ALTER TABLE `elements` ENABLE KEYS */;

-- Struktúra mentése tábla fuzzyfta. events
DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(1024) DEFAULT NULL,
  `value` float DEFAULT 0.5,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='events table';

-- Tábla adatainak mentése fuzzyfta.events: ~3 rows (hozzávetőleg)
DELETE FROM `events`;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` (`id`, `description`, `value`) VALUES
	(1, 'Door not locked', 0.5),
	(2, 'Door locking mechanism power outage', 0.5),
	(3, 'Alert light not working', 0.5);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;

-- Struktúra mentése tábla fuzzyfta. lines
DROP TABLE IF EXISTS `lines`;
CREATE TABLE IF NOT EXISTS `lines` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `element_id` int(11) DEFAULT NULL,
  `begin-x` float DEFAULT NULL,
  `begin-y` float DEFAULT NULL,
  `end-x` float DEFAULT NULL,
  `end-y` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `element_id` (`element_id`),
  CONSTRAINT `element_id` FOREIGN KEY (`element_id`) REFERENCES `elements` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Tábla adatainak mentése fuzzyfta.lines: ~0 rows (hozzávetőleg)
DELETE FROM `lines`;
/*!40000 ALTER TABLE `lines` DISABLE KEYS */;
/*!40000 ALTER TABLE `lines` ENABLE KEYS */;

-- Struktúra mentése tábla fuzzyfta. relations
DROP TABLE IF EXISTS `relations`;
CREATE TABLE IF NOT EXISTS `relations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `members` varchar(50) DEFAULT NULL,
  `logicgate` enum('or','and') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Tábla adatainak mentése fuzzyfta.relations: ~3 rows (hozzávetőleg)
DELETE FROM `relations`;
/*!40000 ALTER TABLE `relations` DISABLE KEYS */;
INSERT INTO `relations` (`id`, `members`, `logicgate`) VALUES
	(1, 'e1,e2', 'or'),
	(2, 'e3,e4', 'and'),
	(3, 'r1,r2', 'and');
/*!40000 ALTER TABLE `relations` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
