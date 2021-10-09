-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table fuzzyfta.elements
CREATE TABLE IF NOT EXISTS `elements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL DEFAULT 1,
  `event_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `event_id` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table fuzzyfta.elements: ~2 rows (approximately)
/*!40000 ALTER TABLE `elements` DISABLE KEYS */;
INSERT INTO `elements` (`id`, `level`, `event_id`) VALUES
	(1, 1, 1);
INSERT INTO `elements` (`id`, `level`, `event_id`) VALUES
	(2, 1, 3);
/*!40000 ALTER TABLE `elements` ENABLE KEYS */;

-- Dumping structure for table fuzzyfta.events
CREATE TABLE IF NOT EXISTS `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(1024) DEFAULT NULL,
  `value` float DEFAULT 0.5,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COMMENT='events table';

-- Dumping data for table fuzzyfta.events: ~3 rows (approximately)
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` (`id`, `description`, `value`) VALUES
	(1, 'Door not locked', 0.5);
INSERT INTO `events` (`id`, `description`, `value`) VALUES
	(2, 'Door locking mechanism power outage', 0.5);
INSERT INTO `events` (`id`, `description`, `value`) VALUES
	(3, 'Alert light not working', 0.5);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;

-- Dumping structure for table fuzzyfta.lines
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Dumping data for table fuzzyfta.lines: ~0 rows (approximately)
/*!40000 ALTER TABLE `lines` DISABLE KEYS */;
/*!40000 ALTER TABLE `lines` ENABLE KEYS */;

-- Dumping structure for table fuzzyfta.relations
CREATE TABLE IF NOT EXISTS `relations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `members` varchar(50) DEFAULT NULL,
  `logicgate` enum('or','and') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table fuzzyfta.relations: ~1 rows (approximately)
/*!40000 ALTER TABLE `relations` DISABLE KEYS */;
INSERT INTO `relations` (`id`, `members`, `logicgate`) VALUES
	(1, '1,2', 'or');
/*!40000 ALTER TABLE `relations` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
