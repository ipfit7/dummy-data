CREATE TABLE `behandelgeschiedenis` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `patientID` int(11) NOT NULL,
  `dentistID` int(11) NOT NULL,
  `treatmentDate` date NOT NULL,
  `behandelID` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
