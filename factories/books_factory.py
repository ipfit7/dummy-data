from util.singleton import Singleton
from models.treatment_model import TreatmentModel
from models.books_model import BooksModel
import datetime
import pandas
import time
import MySQLdb

class BookFactory(metaclass=Singleton):
    def __init__(self):
        self.db = MySQLdb.connect(host='127.0.0.1', user='root', database='boekhouding')
        self.c = self.db.cursor()

    def make_tables(self):
        for n in range(1991,2020):
            create = """CREATE TABLE `Y{0}` (
            `ID` int(11) NOT NULL AUTO_INCREMENT,
            `inkomsten` double NOT NULL,
            `uitgaven` double NOT NULL,
            `btw` double NOT NULL,
            `inkomsten_belasting` double NOT NULL,
            `kwartaal` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
            `inkomst_datum` date NOT NULL,
            PRIMARY KEY (`ID`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
            """.format(n)
            self.c.execute(create)
            self.db.commit()

    def make_books(self, treatments: TreatmentModel) -> None:
        self.books = BooksModel()
        for treatment in treatments:
            year = "Y{0}".format(treatment.treatmentDate.year)
            app_date = treatment.treatmentDate
            app_date_year = int(app_date.strftime("%Y"))
            app_date_month = int(app_date.strftime("%m"))
            app_date_day = int(app_date.strftime("%d"))
            quart = pandas.Timestamp(datetime.date(app_date_year, app_date_month, app_date_day)).quarter
            if quart == 1:
                self.books.quarter = "q1"
                self.books.income = treatment.treatmentCost
                self.books.vat = 0.21 * self.books.income
                self.books.tax = 0.40 * self.books.income
            elif quart == 2:
                self.books.quarter = "q2"
                self.books.income = treatment.treatmentCost
                self.books.vat = 0.21 * self.books.income
                self.books.tax = 0.40 * self.books.income
            elif quart == 3:
                self.books.quarter = "q3"
                self.books.income = treatment.treatmentCost
                self.books.vat = 0.21 * self.books.income
                self.books.tax = 0.40 * self.books.income
            elif quart == 4:
                self.books.quarter = "q4"
                self.books.income = treatment.treatmentCost
                self.books.vat = 0.21 * self.books.income
                self.books.tax = 0.40 * self.books.income
            
            querry = "INSERT INTO {0} (inkomsten, uitgaven, btw, inkomsten_belasting, kwartaal, inkomst_datum) VALUES (%s, %s, %s, %s, %s, %s)".format(year)
            values = (format(self.books.income, ".2f"), format(self.books.expence, ".2f"), format(self.books.vat, ".2f"),
                format(self.books.tax, ".2f"), self.books.quarter, treatment.treatmentDate)
            self.c.execute(querry, values)
            self.db.commit()
        
        
        
