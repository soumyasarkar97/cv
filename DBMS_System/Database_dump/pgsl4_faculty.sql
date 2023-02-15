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
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `f_id` varchar(25) NOT NULL,
  `name` varchar(45) NOT NULL,
  `dep` varchar(10) NOT NULL,
  `designation` varchar(45) NOT NULL,
  `j_date` date DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES ('abhinav.dhall','Abhinav Dhall','CSE','Associate','2012-04-24',9655245889,'abhinav.dhall@cse.iitrpr.ac.in'),('apurva.mudgal','Apurva Mudgal','CSE','Associate','2012-04-24',9000240880,'apurva.mudgal@cse.iitrpr.ac.in'),('deepti.bathula','Deepthi Bathula','CSE','Associate','2012-04-24',9077212221,'deepti.bathula@cse.iitrpr.ac.in'),('mukesh.saini','Mukesh Saini','CSE','Assistant','2012-04-24',9727776225,'mukesh.saini@cse.iitrpr.ac.in'),('neeraj.goel','Neeraj Goel','CSE','Assistant','2012-04-24',8892199001,'neeraj.goel@cse.iitrpr.ac.in'),('puneet.goyal','Puneet Goyal','CSE','Associate','2012-04-24',9044636522,'puneet.goyal@cse.iitrpr.ac.in'),('shashi.jha','Shashi Jha','CSE','Assistant','2012-04-24',8911078256,'shashi.jha@cse.iitrpr.ac.in'),('shirshendu.das','Shirshendu Das','CSE','Associate','2012-04-24',9036744321,'shirshendu.das@cse.iitrpr.ac.in'),('shweta.jain','Shweta Jain','CSE','Assistant','2012-04-24',9034566211,'shweta.jain@cse.iitrpr.ac.in'),('sudeepta.mishra','Sudeepta Mishra','CSE','Assistant','2012-04-24',9726612345,'sudeepta.mishra@cse.iitrpr.ac.in'),('sujata.pal','Sujata Pal','CSE','Assistant','2012-04-24',9024511356,'sujata.pal@cse.iitrpr.ac.in'),('vishwanath.gunturi','Vishwanath Gunturi','CSE','Assistant','2012-04-24',8776190345,'vishwanath.gunturi@cse.iitrpr.ac.in');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
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
