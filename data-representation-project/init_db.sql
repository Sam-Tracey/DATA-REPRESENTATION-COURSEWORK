/* Check to see if the dataRepresentation table exists. If it does, then the database has already been initialized. */
CREATE DATABASE  IF NOT EXISTS `datarepresentation`;
USE `datarepresentation`;

/* Create unemployment table consiting of Date as Primary key and Unemployment Rate as a float */
CREATE TABLE IF NOT EXISTS `unemployment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL UNIQUE,
  `unemploymentRate` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/* Create mfgEmployees table consiting of Date as Primary key and num_employees as a float */
CREATE TABLE IF NOT EXISTS `mfgEmployees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL UNIQUE,
  `num_employees` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/* Create quits table consiting of Date as Primary key and num_employees as a float */
CREATE TABLE IF NOT EXISTS `quits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL UNIQUE,
  `num_quits` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/* Create jobOpenings table consiting of Date as Primary key and num_employees as a float */
CREATE TABLE IF NOT EXISTS `jobOpenings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL UNIQUE,
  `num_openings` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/*Create table localAttritionRate with Date as Primary Key and num_quit as an int*/
CREATE TABLE IF NOT EXISTS `localAttritionRate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL UNIQUE,
  `num_quit` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


/*Create user table consisting of id as primary key, username, password, and email*/
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;