-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `restaurant` (
  `pizza` int(5) DEFAULT NULL,
  `burger` int(5) DEFAULT NULL,
  `fries` int(5) DEFAULT NULL,
  `sandwich` int(5) DEFAULT NULL,
  `noodles` int(5) DEFAULT NULL,
  `friedrice` int(5) DEFAULT NULL,
  `lakesidesp` int(5) DEFAULT NULL,
  `vegmeal` int(5) DEFAULT NULL,
  `novegmeal` int(5) DEFAULT NULL,
  `costofmeal` varchar(20) NOT NULL,
  `servicecharge` varchar(20) NOT NULL,
  `tax` varchar(20) NOT NULL,
  `totalcost` varchar(20) NOT NULL,
  `drinks` int(20) DEFAULT NULL,
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `reference` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant`
--

LOCK TABLES `restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant` DISABLE KEYS */;
INSERT INTO `restaurant` VALUES (1,0,0,1,0,0,0,0,0,'230','2','46.0','278.0',0,1,'330900'),(1,0,0,0,0,0,0,0,0,'180','1','36.0','217.0',0,20,'398400'),(2,0,2,0,0,0,0,0,2,'980','9','196.0','1185.0',1,21,'325300'),(2,0,0,2,0,0,0,0,0,'460','4','92.0','556.0',0,22,'344000'),(1,0,1,1,1,0,0,0,0,'360','3','72.0','435.0',0,23,'420600'),(1,1,1,1,0,0,0,0,0,'360','3','72.0','435.0',0,24,'203400'),(1,2,0,1,0,0,0,0,7,'1910','19','382.0','2311.0',0,25,'564900'),(1,0,1,0,1,0,0,0,1,'530','5','106.0','641.0',0,26,'397400');
/*!40000 ALTER TABLE `restaurant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-15  9:59:17
