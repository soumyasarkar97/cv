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
-- Table structure for table `faculty_course_mapping`
--

DROP TABLE IF EXISTS `faculty_course_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty_course_mapping` (
  `c_id` varchar(10) NOT NULL,
  `f_id` varchar(25) NOT NULL,
  `min_gpa` decimal(10,3) NOT NULL,
  `sem` int NOT NULL,
  `year` int NOT NULL,
  PRIMARY KEY (`c_id`),
  KEY `f_id` (`f_id`),
  CONSTRAINT `faculty_course_mapping_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `course_catalogue` (`c_id`),
  CONSTRAINT `faculty_course_mapping_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `faculty` (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_course_mapping`
--

LOCK TABLES `faculty_course_mapping` WRITE;
/*!40000 ALTER TABLE `faculty_course_mapping` DISABLE KEYS */;
INSERT INTO `faculty_course_mapping` VALUES ('CS301','vishwanath.gunturi',0.000,3,22),('CS302','apurva.mudgal',8.000,3,22),('CS504','abhinav.dhall',8.000,3,22),('CS506','puneet.goyal',7.000,3,22),('CS509','vishwanath.gunturi',0.000,3,22),('CS510','shirshendu.das',8.000,3,22),('CS516','sujata.pal',6.000,3,22),('CS517','deepti.bathula',6.000,3,22),('CS518','abhinav.dhall',7.000,3,22),('CS526','shweta.jain',7.000,3,22),('CS527','neeraj.goel',6.000,3,22),('CS533','shashi.jha',8.000,3,22),('CS539','sudeepta.mishra',6.000,3,22),('CS550','mukesh.saini',0.000,3,22),('CS994','shweta.jain',6.000,3,23),('CS996','shweta.jain',3.000,4,24),('CS997','shweta.jain',9.000,3,23);
/*!40000 ALTER TABLE `faculty_course_mapping` ENABLE KEYS */;
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
