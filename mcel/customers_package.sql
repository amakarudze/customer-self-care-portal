-- MySQL dump 10.13  Distrib 5.6.24, for Win32 (x86)
--
-- Host: localhost    Database: customers
-- ------------------------------------------------------
-- Server version	5.6.25-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `package`
--

DROP TABLE IF EXISTS `package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `package` (
  `idPackage` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(45) DEFAULT NULL,
  `pdescription` varchar(120) DEFAULT NULL,
  `ptype` varchar(15) DEFAULT NULL,
  `category` varchar(15) DEFAULT NULL,
  `minutes` int(11) DEFAULT NULL,
  `datamb` int(11) DEFAULT NULL,
  `sms` int(11) DEFAULT NULL,
  `monthlyfee` float DEFAULT NULL,
  `gadget` char(3) DEFAULT NULL,
  `gadgettype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPackage`),
  UNIQUE KEY `idPackages_UNIQUE` (`idPackage`),
  UNIQUE KEY `pname_UNIQUE` (`pname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package`
--

LOCK TABLES `package` WRITE;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
INSERT INTO `package` VALUES (1,'Ola 30','The lowest NTDUO package offered by mcel. NTDUO packages are both prepaid and postpaid.','Individual','NTDUO',30,100,50,300,'No',NULL),(2,'Ola 60','This is the lowest postpaid package offered by mcel.','Individual','Postpaid',60,200,80,450,'No',NULL),(3,'Ola 120','An NTDUO package which offers more benefits to the customer.','Individual','NTDUO',120,512,200,800,'Yes','Samsung Galaxy Pocket'),(4,'Ola 500','An executive postpaid package which offers more benefits to the customer.','Individual','Postpaid',120,2048,300,1500,'Yes','Samsung Galaxy Note 3');
/*!40000 ALTER TABLE `package` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-27 14:52:23
