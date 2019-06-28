CREATE TABLE `behandelingen` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `behandelID` int(11) NOT NULL,
  `behandelDesc` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `behandelCost` double NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
