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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `idCustomer` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL,
  `dateofbirth` varchar(12) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `idtype` varchar(15) DEFAULT NULL,
  `idnum` varchar(14) DEFAULT NULL,
  `phonenum` varchar(15) DEFAULT NULL,
  `mobilenum` varchar(15) DEFAULT NULL,
  `emailaddress` varchar(120) DEFAULT NULL,
  `address1` varchar(100) DEFAULT NULL,
  `address2` varchar(100) DEFAULT NULL,
  `towncity` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `prefchannel` varchar(15) DEFAULT NULL,
  `existingcustomer` char(3) DEFAULT NULL,
  `msisdns` varchar(100) DEFAULT NULL,
  `employment` varchar(45) DEFAULT NULL,
  `employer` varchar(100) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `companysize` varchar(20) DEFAULT NULL,
  `employmenttenure` varchar(15) DEFAULT NULL,
  `monthlyincome` float DEFAULT NULL,
  `accounttype` varchar(15) DEFAULT NULL,
  `accountnum` varchar(25) DEFAULT NULL,
  `bankname` varchar(25) DEFAULT NULL,
  `branch` varchar(25) DEFAULT NULL,
  `currency` varchar(3) DEFAULT NULL,
  `yearsopen` int(11) DEFAULT NULL,
  `monthsopen` int(11) DEFAULT NULL,
  `bankcertname` varchar(15) DEFAULT NULL,
  `bankcertpos` varchar(15) DEFAULT NULL,
  `billingtype` varchar(25) DEFAULT NULL,
  `billingaccount` varchar(25) DEFAULT NULL,
  `securitynum` varchar(5) DEFAULT NULL,
  `billemail` tinyint(1) DEFAULT NULL,
  `receivepromos` tinyint(1) DEFAULT NULL,
  `promoby` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`idCustomer`),
  UNIQUE KEY `natid_UNIQUE` (`idnum`),
  UNIQUE KEY `emailaddress_UNIQUE` (`emailaddress`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Mufaro','Makarudze',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'mmakarudze@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'Anna','Makarudze','F','1986-06-30','Zimbabwean','Passport','DN135052','823525528','823525528','amakarudze@gmail.com','4th Floor, Flat 3','Avenida 24 de Julho','Maputo','Mozambique','SMS','Yes','823525528','Self-Employed','Anntele Business Solutions','Managing Consultant','0-10','0-2',12000,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'Jonas','Alberto Junior','M','1981-03-11','Mozambican','Moz ID','56790H4567',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'Genius Addmore','Makarudze','M','1991-05-11','Zimbabwean','Passport','DZ123052',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Philly','Mandiza','M','1981-04-15','Malawian','Passport','DWZ13647483','826787148','827044881','pmandiza@mcel.co.mz','5th Floor, Flat 2','Avenida 24 de Julho','Maputo','Mozambique','Phone',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-27 14:52:22
