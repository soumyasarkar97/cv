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
-- Table structure for table `login_details`
--

DROP TABLE IF EXISTS `login_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_details` (
  `user_id` varchar(25) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  `user_type` int NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_details`
--

LOCK TABLES `login_details` WRITE;
/*!40000 ALTER TABLE `login_details` DISABLE KEYS */;
INSERT INTO `login_details` VALUES ('2021csm1001','$2b$12$S33D7aEnbHVfSHIMNnSqt.Waof9fNoQlFbuyJtfI7PoWwdTIqiJI2',3),('2021csm1002','$2b$12$.N3m8jmXrm7sVixEMldzOOJYKbVTx1q4tjxSIsoTfM5z9qfirGoOO',3),('2021csm1003','$2b$12$emWu8K3SNghtRqInDtg/SeR5rLvCWcwJDInCsOh133briusgz8p72',3),('2021csm1004','$2b$12$AdRQ248ewDSBjyLgK7qNduYXad7Q0xU4WwmegxI6oFweCyCwA6OS.',3),('2021csm1005','$2b$12$.HhZurOVRgFhv7uUqKOwfuI7RWfyVmVXnyPtizIiqzoIu7FsLHa4e',3),('2021csm1006','$2b$12$raGguAegspR0phlnZkfJsuqGfXsjusPogf97VIO5jY8stfSIQsfS2',3),('2021csm1007','$2b$12$XfoZfiMSs.teRXA4CUagButZDurc1Tw6oOOBQLE3qywA3ZnEMfnDi',3),('2021csm1008','$2b$12$gyWfovmeaTWNzCPmUUNaBO08cVGQt2gzbKDZDOttQxYiYEjKeVISi',3),('2021csm1009','$2b$12$F0vqYVup0nldFQC8YnIQXulshtRJ6Zw/OzlL0Vp5W0pTSQzpkNTN6',3),('2021csm1010','$2b$12$TQns57Bp5kt8MfN8TSTRAeYjwFEHiph51Nll.f6Q7RiyN.p.hSZ1S',3),('2021csm1011','$2b$12$JrWAf6EkRiSEuM4savUAAuKC0cHDUwPyHybZhKnZQQN.bpy9lxUme',3),('2021csm1012','$2b$12$Fx57RZ3MzLiJMygyWd0JMeV8czzIjWtaDY0Me0BTxt3yeuhT5PKKC',3),('2021csm1013','$2b$12$aFDTypvlS6MFVxTtl7utOuzHRBnVPkSR2rEWySHZhCNQgbrVDUOmm',3),('2021csm1014','$2b$12$5SldAGUSriSJUIRIUhQIru8mvloJ2OhMLETA9C5OVQaqCikpAdk.y',3),('2021csm1015','$2b$12$9CHYu1EqVhEMwHwkncdPauCkowriwPpGWkZGewUBSuCmpakwov/Iy',3),('abhinav.dhall','$2b$12$ByQOGeMRAErFWzIl2VqJIuzioZdTEd9EyAJOza7fHprLchK.HcI6q',2),('apurva.mudgal','$2b$12$E/zLLnV0NBevCEX/fEljNuKgUqJdlTMyhQRLsjEzq8XmiowdUnNKm',2),('deepti.bathula','$2b$12$mm41j7f2uup0kQlwWx4vCOqRF322r5BgnMNtSPk2fhBA8uWsHExrS',2),('juhi.goyal','$2b$12$VAfPT0PVjqc9PFHerYeXVe8hUMD3WThmngyfBYhbQWoZZ89mTyxWm',1),('mukesh.saini','$2b$12$lAslDsKnkw8szXujrFC1uOgT00v/yVUiBtd2WZ2VS4I.GPp8zyHX6',2),('neeraj.goel','$2b$12$Ac5FmwqOQTyF2ElUAU2aYOpgAUehciqgpArOepkqV1uxeWTkDhoM.',2),('puneet.goyal','$2b$12$OPE2EdFL9JGOuNEmX01U4.bp9ohO/qiA3xJ26oUkr4kYQU9Mlr4PG',2),('shashi.jha','$2b$12$Q6qYm3fPq9hgjRqL7skceeNaCQ9TAyINyrmxJpbd9ZdR03t48ycc.',2),('shirshendu.das','$2b$12$HUZm8/3QkGKiq/wIeCW9wOTSNmJLjvOz6.DQRSJisDMUmiHUFSfDG',2),('shweta.jain','$2b$12$vhSK/jyx7icm7/BumBXG8Oucbayr2KmJ.f90Tl6xnttOY/aqyZe6G',2),('staff.dean','$2b$12$RCW/y0c2RHqGWRQruHamIe.VqVrqE0P.vbN/It0LomX.z9FtDyeq.',1),('sudeepta.mishra','$2b$12$JjjlTtV8X6NIIxJ4gn6PCeq.zXs9lncQxRGkp6qCnIGjRHXeJkd8m',2),('sudipta.mishra','$2b$12$Ou14FQQ6WHMzBCjRBSOK3.obR1g03c2d.ogslD0sHEa8ZQrjO9aEW',1),('sujata.pal','$2b$12$yFQzmWNywVrhvr2ehJRbMespQVBSv8BciuI7jF.Icvfc8f0Id81DG',2),('vishwanath.gunturi','$2b$12$6dGZ0gHHoiFbfvM.l/iM7.0aUhGmG8MlIAxSncafr1tojUtuV9tGu',2);
/*!40000 ALTER TABLE `login_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-26 23:58:18
