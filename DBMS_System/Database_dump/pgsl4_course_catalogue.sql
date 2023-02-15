-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: pgsl4
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course_catalogue`
--

DROP TABLE IF EXISTS `course_catalogue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_catalogue` (
  `c_id` varchar(10) NOT NULL,
  `cname` varchar(50) NOT NULL,
  `L` int NOT NULL,
  `T` int NOT NULL,
  `P` int NOT NULL,
  `S` int NOT NULL,
  `C` int NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_catalogue`
--

LOCK TABLES `course_catalogue` WRITE;
/*!40000 ALTER TABLE `course_catalogue` DISABLE KEYS */;
INSERT INTO `course_catalogue` VALUES ('CS301','Databases',3,1,2,6,4),('CS302','Analysis and Design of Algorithms',3,1,0,5,3),('CS504','ARTIFICIAL NEURAL NETWORKS',2,0,2,5,3),('CS506','DATA STRUCTURES AND ALGORITHM',3,1,2,6,4),('CS507','MULTIMEDIA SYSTEMS',2,0,2,5,3),('CS509','PG SOFTWARE LAB',0,0,6,3,3),('CS510','ADVANCED COMPUTER ARCHITECTURE',3,1,0,5,3),('CS516','Wireless Adhoc Networks',2,0,2,5,3),('CS517','DIGITAL IMAGE PROCESSING & ANALYSIS',2,1,2,4,3),('CS518','COMPUTER VISION',2,0,2,5,3),('CS526','MATHEMATICAL FOUNDATION OF COMPUTER SCIENCE',3,1,0,5,3),('CS527','COMPUTER SYSTEMS',3,0,2,7,4),('CS533','REINFORCEMENT LEARNING',3,0,0,6,3),('CS539','Internet of Things',3,0,0,6,3),('CS550','RESEARCH METHODOLOGY IN COMPUTER SCIENCE',1,0,0,2,1),('CS991','Dummy Course 9',3,2,3,6,5),('CS992','Dummy Course 8',4,2,1,7,5),('CS993','Dummy Course 7',8,7,3,11,10),('CS994','Dummy Course 6',3,3,3,5,5),('CS995','Dummy Course 5',3,2,0,4,3),('CS996','Dummy Course 4',4,0,0,8,4),('CS997','Dummy Course 3',3,0,2,7,4),('CS998','Dummy Course 2',4,0,2,9,5),('CS999','Dummy Course 1',3,2,2,5,4);
/*!40000 ALTER TABLE `course_catalogue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26 23:58:07
