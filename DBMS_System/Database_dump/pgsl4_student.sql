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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `s_id` varchar(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `dep` varchar(10) NOT NULL,
  `j_date` date DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('2021csm1001','Yakul Dogra','CSE','2021-07-27',9705123455,'2021csm1001@cse.iitrpr.ac.in'),('2021csm1002','Soumya Sarkar','CSE','2021-07-27',8911027542,'2021csm1002@cse.iitrpr.ac.in'),('2021csm1003','Kumar Mangalam','CSE','2021-07-27',9765416126,'2021csm1003@cse.iitrpr.ac.in'),('2021csm1004','Piyush Agrawal','CSE','2021-07-27',9128379181,'2021csm1004@cse.iitrpr.ac.in'),('2021csm1005','Saksham Srivastava','CSE','2021-07-27',9127363812,'2021csm1005@cse.iitrpr.ac.in'),('2021csm1006','Virat Aggarwal','CSE','2021-07-27',9705000455,'2021csm1006@cse.iitrpr.ac.in'),('2021csm1007','Nitin Singhal','CSE','2021-07-27',8911027002,'2021csm1007@cse.iitrpr.ac.in'),('2021csm1008','Karan Singh','CSE','2021-07-27',9712316126,'2021csm1008@cse.iitrpr.ac.in'),('2021csm1009','Jordan Dreyer','CSE','2021-07-27',9127365716,'2021csm1009@cse.iitrpr.ac.in'),('2021csm1010','Juhi Chawla','CSE','2021-07-27',9126126624,'2021csm1010@cse.iitrpr.ac.in'),('2021csm1011','Virat Kohli','CSE','2021-07-27',9126125533,'2021csm1011@cse.iitrpr.ac.in'),('2021csm1012','Tenali Raman','CSE','2021-07-27',9737376227,'2021csm1012@cse.iitrpr.ac.in'),('2021csm1013','Protichi Das','CSE','2021-07-27',9712726262,'2021csm1013@cse.iitrpr.ac.in'),('2021csm1014','Manish Sarkar','CSE','2021-07-27',9883827271,'2021csm1014@cse.iitrpr.ac.in'),('2021csm1015','Narendra Lodi','CSE','2021-07-27',9010636101,'2021csm1015@cse.iitrpr.ac.in');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
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
