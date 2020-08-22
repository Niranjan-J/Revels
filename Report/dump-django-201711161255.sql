-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: django
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

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
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(200) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,'Movies'),(2,'Educational'),(3,'Entertainment'),(4,'Documentary'),(5,'Mystery/Thriller'),(6,'Infotainment'),(7,'News'),(8,'Comedy'),(9,'Sports'),(10,'Live'),(11,'Music');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Channel`
--

DROP TABLE IF EXISTS `Channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Channel` (
  `channel_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`channel_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Channel_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Channel`
--

LOCK TABLES `Channel` WRITE;
/*!40000 ALTER TABLE `Channel` DISABLE KEYS */;
INSERT INTO `Channel` VALUES (1,'Web Development','Learn web devlopment and develope your own websites....',1),(2,'Machine Learning','Make machines intelligent....',1),(3,'Mathematics','All Maths for programmers',2),(4,'Competitive Programming','Learn to compete in Programming.....',2),(5,'Suspense Thrillers','Get thrilled...!!',3),(6,'Action Movies','Meet your favrite superheroes',3),(7,'Michael Jackson','Here\'s the legend....',3);
/*!40000 ALTER TABLE `Channel` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER channelDeleteTrigger
BEFORE DELETE ON Channel
FOR EACH ROW
BEGIN
DELETE FROM Playlist WHERE OLD.channel_id = channel_id;
DELETE FROM Subscription WHERE OLD.channel_id = channel_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Comment`
--

DROP TABLE IF EXISTS `Comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(2000) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `video_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `video_id` (`video_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Comment_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `Video` (`video_id`),
  CONSTRAINT `Comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment`
--

LOCK TABLES `Comment` WRITE;
/*!40000 ALTER TABLE `Comment` DISABLE KEYS */;
INSERT INTO `Comment` VALUES (2,'That was helpful !!','2017-11-16 07:20:24',13,1),(3,'That was helpful !!','2017-11-16 07:20:31',5,1),(4,'That was helpful !!','2017-11-16 07:20:35',6,1),(5,'That was helpful !!','2017-11-16 07:20:42',11,1),(6,'That was helpful !!','2017-11-16 07:20:49',10,1),(7,'That was helpful !!','2017-11-16 07:20:57',9,1),(8,'That was helpful !!','2017-11-16 07:21:03',8,1),(9,'That was helpful !!','2017-11-16 07:21:11',7,1);
/*!40000 ALTER TABLE `Comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Like`
--

DROP TABLE IF EXISTS `Like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Like` (
  `video_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  KEY `video_id` (`video_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Like_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `Video` (`video_id`),
  CONSTRAINT `Like_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Like`
--

LOCK TABLES `Like` WRITE;
/*!40000 ALTER TABLE `Like` DISABLE KEYS */;
INSERT INTO `Like` VALUES (13,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1);
/*!40000 ALTER TABLE `Like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pl_Vid`
--

DROP TABLE IF EXISTS `Pl_Vid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pl_Vid` (
  `video_id` int(11) DEFAULT NULL,
  `playlist_id` int(11) DEFAULT NULL,
  UNIQUE KEY `playlist_id` (`playlist_id`,`video_id`),
  KEY `video_id` (`video_id`),
  CONSTRAINT `Pl_Vid_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `Video` (`video_id`),
  CONSTRAINT `Pl_Vid_ibfk_2` FOREIGN KEY (`playlist_id`) REFERENCES `Playlist` (`playlist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pl_Vid`
--

LOCK TABLES `Pl_Vid` WRITE;
/*!40000 ALTER TABLE `Pl_Vid` DISABLE KEYS */;
INSERT INTO `Pl_Vid` VALUES (6,1),(7,1),(9,2),(10,2),(11,3),(13,4),(5,6);
/*!40000 ALTER TABLE `Pl_Vid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Playlist`
--

DROP TABLE IF EXISTS `Playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Playlist` (
  `playlist_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `channel_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`playlist_id`),
  KEY `channel_id` (`channel_id`),
  CONSTRAINT `Playlist_ibfk_1` FOREIGN KEY (`channel_id`) REFERENCES `Channel` (`channel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Playlist`
--

LOCK TABLES `Playlist` WRITE;
/*!40000 ALTER TABLE `Playlist` DISABLE KEYS */;
INSERT INTO `Playlist` VALUES (1,'Django for Web Development',1),(2,'HTML5 and CSS3',1),(3,'Javascript-Fronend',1),(4,'Angular JS',1),(5,'Data Structures',4),(6,'C++ STL',4),(7,'More On Trees And Graphs',4),(8,'Types of Algorithms',4),(9,'Sorting',4),(10,'Matrices',3),(11,'Combinatorics',3),(12,'Functions And Relations',3);
/*!40000 ALTER TABLE `Playlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER playlistDeleteTrigger
BEFORE DELETE ON Playlist
FOR EACH ROW
BEGIN
DELETE FROM Pl_Vid WHERE OLD.playlist_id = playlist_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Profile`
--

DROP TABLE IF EXISTS `Profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile` (
  `user_id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `avatar` varchar(200) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `firstname` (`firstname`,`lastname`,`avatar`),
  CONSTRAINT `Profile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile`
--

LOCK TABLES `Profile` WRITE;
/*!40000 ALTER TABLE `Profile` DISABLE KEYS */;
INSERT INTO `Profile` VALUES (1,'Kanishkar','J','M','Hey! This is Kanishar'),(2,'Niranjan','Joshi','M','Hi!'),(3,'Ravi','S','M','Hello everyone !');
/*!40000 ALTER TABLE `Profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sessions`
--

DROP TABLE IF EXISTS `Sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sessions` (
  `user_id` int(11) NOT NULL,
  `session_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `Sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sessions`
--

LOCK TABLES `Sessions` WRITE;
/*!40000 ALTER TABLE `Sessions` DISABLE KEYS */;
INSERT INTO `Sessions` VALUES (1,'b\'$\\xcd\\xf9?yl\\xca(\\x16\\xeb^V8\\xb1@\\x05\''),(2,'b\'O\\xd31\\xef\\xfa\\x86g\\xd5d$k\\t\\xd5P\\x89\\xe4\''),(4,'b\'OH\\x8d\\xd6\\xa1.\\x16\\xdc\\x00\\xb3s\\xae\\xa5\\x7fk\\x9d\''),(5,'b\'\\xe6,\\xed\\x08L\\xa6\\xca9\\xe8\\xb0\\x11%z;gX\''),(7,'b\'N\\xfa\\xcd\\x8cY\\xc0\\xcc=_\\xbb\\xa5\\x8f\\x08\\xcfR\\t\'');
/*!40000 ALTER TABLE `Sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Subscription`
--

DROP TABLE IF EXISTS `Subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Subscription` (
  `user_id` int(11) DEFAULT NULL,
  `channel_id` int(11) DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `channel_id` (`channel_id`),
  CONSTRAINT `Subscription_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `Subscription_ibfk_2` FOREIGN KEY (`channel_id`) REFERENCES `Channel` (`channel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Subscription`
--

LOCK TABLES `Subscription` WRITE;
/*!40000 ALTER TABLE `Subscription` DISABLE KEYS */;
INSERT INTO `Subscription` VALUES (1,3),(1,4),(1,6);
/*!40000 ALTER TABLE `Subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tag`
--

DROP TABLE IF EXISTS `Tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tag` (
  `video_id` int(11) NOT NULL,
  `tag` varchar(200) NOT NULL,
  PRIMARY KEY (`video_id`,`tag`),
  CONSTRAINT `Tag_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `Video` (`video_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tag`
--

LOCK TABLES `Tag` WRITE;
/*!40000 ALTER TABLE `Tag` DISABLE KEYS */;
INSERT INTO `Tag` VALUES (5,'C++'),(5,'Competitive Programming'),(5,'STL'),(6,' HTML'),(6,' Python'),(6,' Web Development'),(6,'Django'),(8,'Data Structures'),(8,'linked list'),(9,' Web Development'),(9,'HTML'),(9,'HTML5'),(10,' CSS3'),(10,' Web Development'),(10,'CSS'),(11,' Javascript'),(11,'Web Development'),(13,' Javascript'),(13,' Web Development'),(13,'Angular');
/*!40000 ALTER TABLE `Tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username_2` (`username`,`email`,`password`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Kanishkar','kani@gmail.com','dd4b21e9ef71e1291183a46b913ae6f2'),(2,'Niranjan','nj@gmail.com','25d55ad283aa400af464c76d713c07ad'),(3,'Ravi','ravi@gmail.com','6eea9b7ef19179a06954edd0f6c05ceb');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `User_Profile`
--

DROP TABLE IF EXISTS `User_Profile`;
/*!50001 DROP VIEW IF EXISTS `User_Profile`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `User_Profile` AS SELECT 
 1 AS `user_id`,
 1 AS `username`,
 1 AS `email`,
 1 AS `password`,
 1 AS `firstname`,
 1 AS `lastname`,
 1 AS `gender`,
 1 AS `avatar`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Vid_Cat`
--

DROP TABLE IF EXISTS `Vid_Cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Vid_Cat` (
  `video_id` int(11) DEFAULT NULL,
  `cat_id` int(11) DEFAULT NULL,
  KEY `video_id` (`video_id`),
  KEY `cat_id` (`cat_id`),
  CONSTRAINT `Vid_Cat_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `Video` (`video_id`),
  CONSTRAINT `Vid_Cat_ibfk_2` FOREIGN KEY (`cat_id`) REFERENCES `Category` (`cat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vid_Cat`
--

LOCK TABLES `Vid_Cat` WRITE;
/*!40000 ALTER TABLE `Vid_Cat` DISABLE KEYS */;
INSERT INTO `Vid_Cat` VALUES (5,2),(5,6),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(13,2);
/*!40000 ALTER TABLE `Vid_Cat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Video`
--

DROP TABLE IF EXISTS `Video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Video` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `descr` text,
  `url` varchar(200) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`video_id`),
  UNIQUE KEY `user_id` (`user_id`,`url`,`title`),
  CONSTRAINT `Video_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Video`
--

LOCK TABLES `Video` WRITE;
/*!40000 ALTER TABLE `Video` DISABLE KEYS */;
INSERT INTO `Video` VALUES (5,'Basic STL','Learn STL features of C++','https://www.youtube.com/embed/Q_y_GdxpKm0',2),(6,'Introduction : Django web development with python 1','Welcome to a Django web development with Python tutorial series. Django is a Python web development framework, aimed at rapid development and deployment.\r\n\r\nOne of the more common questions people have is \"which framework\" they should use. There are quite a few for Python, with Django and Flask being the two most popular.\r\n\r\nFlask is more of what we call a \"micro\" web framework. It is much \"lower level\" than Django is. This allows for more customization and control for the developer.\r\n\r\nDjango is much more of a higher-level framework, and imposes a set structure on the developer.\r\n\r\nThus, with Flask you can create systems your way, which is probably not most efficient, fastest, or secure way. With Django, you are a bit more constrained, but you are going to most likely do it the best way possible. As with almost all questions people ask me regarding which to use, the answer is: Try a few, and choose the one you like best. In the end, Django and Flask can be used to make the exact same websites!\r\n\r\nTo try Django, you need to get Django first (you will also need Python installed). This is exceptionally simple:\r\n\r\npip install Django.','https://www.youtube.com/embed/FNQxxpM1yOs',1),(7,'Django Web Development with Python 2','Welcome to the second Django web development with Python tutorial. This tutorial picks up from the previous one, and is focused on getting a simple page to render some text. After you did the startproject command, a new directory is created, called whatever you named it. We called it mysite. Change directory into your new directory cd mysite. Next, we create a new app for this:\r\n\r\npython manage.py startapp webapp\r\n\r\nNow a new directory exists, called webapp. In here, we see a lot of similar files, and some new ones:\r\n\r\nwebapp/\r\n    migrations/ \r\n __init__.py\r\n admin.py\r\n apps.py\r\n models.py\r\n tests.py\r\n views.py\r\nThe app is indeed treated as its own package, with its own __init__.py, along with other files. For now, we will concern ourselves with views.py, and we\'re actually going to add another file urls.py.','https://www.youtube.com/embed/iZ5my3krEVM',1),(8,'Introduction to Linked Lists','Learn use of linked list','https://www.youtube.com/embed/pBrz9HmjFOs',2),(9,'HTML Crash Course For Absolute Beginners','In this crash course I will cram as much about HTML that I can. This is meant for absolute beginners. If you are interested in learning HTML but know nothing, then you are in the right place. We will be creating a cheat sheet with all of the common HTML5 tags, attributes, semantic markup, etc. We will not be focusing on CSS in this video. The CSS crash course will be released shortly after','https://www.youtube.com/embed/UB1O30fR-EE',1),(10,'CSS Crash Course For Absolute Beginners','In this video I will cram as much as possible about CSS. We will be looking at styles, selectors, declarations, etc. We will build a CSS cheat sheet that you can keep as a resource and we will also create a basic website layout. We are using CSS3 but mostly the basics. I will be creating an advanced CSS course with animations,  etc. I do have a Flexbox in 20 minutes video as well if you want to learn flexbox.','https://www.youtube.com/embed/yfoY53QXEnI',1),(11,'JavaScript Fundamentals For Beginners','This is a mini-course on the fundamentals of not only JavaScript, but programming in general. We will cover the following...\r\n\r\nWhat is JavaScript?\r\nVariables & Data Types\r\nLoops\r\nArrays\r\nObjects\r\nFunctions\r\nConditionals - If Statements, switches\r\nEvents\r\nForms & Validation','https://www.youtube.com/embed/vEROU2XtPR8',1),(13,'Angular 4 In 60 Minutes','In this Angular 4 crash course we will be diving into the latest version of the Angular framework and look at all the fundamentals including Angular CLI, components, services, types, directives, events, HTTP, routing and more','https://www.youtube.com/embed/KhzGSHNhnbI',1);
/*!40000 ALTER TABLE `Video` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER videoDeleteTrigger
              BEFORE DELETE ON Video
                     FOR EACH ROW
                     BEGIN
                       DELETE FROM Tag WHERE OLD.video_id = video_id;
                       DELETE FROM Vid_Cat WHERE OLD.video_id = video_id;
                       DELETE FROM Pl_Vid WHERE OLD.video_id = video_id;
                       DELETE FROM Comment WHERE OLD.video_id = video_id;
                       DELETE FROM `Like` WHERE OLD.video_id = video_id;
                     END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'django'
--
/*!50003 DROP PROCEDURE IF EXISTS `insertTag` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`django`@`localhost` PROCEDURE `insertTag`( IN tag VARCHAR(100), IN video_id INT )
BEGIN
                INSERT INTO Tag(video_id, tag) VALUES(video_id, tag) ;
              END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `User_Profile`
--

/*!50001 DROP VIEW IF EXISTS `User_Profile`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`django`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `User_Profile` AS select `User`.`user_id` AS `user_id`,`User`.`username` AS `username`,`User`.`email` AS `email`,`User`.`password` AS `password`,`Profile`.`firstname` AS `firstname`,`Profile`.`lastname` AS `lastname`,`Profile`.`gender` AS `gender`,`Profile`.`avatar` AS `avatar` from (`User` join `Profile` on((`User`.`user_id` = `Profile`.`user_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-16 12:55:13
