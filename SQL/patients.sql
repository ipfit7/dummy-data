CREATE TABLE `patients` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `middleName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `bsn` int(11) NOT NULL,
  `dateOfBirth` date NOT NULL,
  `address` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `placeOfResidence` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
