CREATE TABLE `tandartsen` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `dentistID` int(11) NOT NULL,
  `dentistFirstName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dentistMiddleName` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dentistLastName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `specialty` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
