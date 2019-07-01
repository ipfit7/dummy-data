from util.singleton import Singleton
from factories.identity_factory import IdentityFactory
from repositories.treatment_repository import TreatmentRepository
from models.treatment_model import TreatmentModel
from models.identity_model import IdentityModel
from models.dentist_model import DentistModel
import MySQLdb

class SQLRepository(metaclass=Singleton):

    def __init__(self):
        self.db = MySQLdb.connect(host='127.0.0.1', user='root', database='patientinfo')
        self.c = self.db.cursor()
        self.id_factory = IdentityFactory()
        
    def insert_patients(self, patient: IdentityModel) -> None:
        querry = "INSERT INTO patients (patientID, firstName, middleName, lastName, bsn, dateOfBirth, address, placeOfResidence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (patient.ID, patient.firstName, patient.middleName, patient.lastName, patient.bsn, patient.dateOfBirth, patient.address,
            patient.placeOfResidence)
        self.c.execute(querry, values)
        self.db.commit()
    
    def insert_treatments(self, treatments: []) -> None:
        querry = "INSERT INTO behandelingen (behandelID, behandelDesc, behandelCost) VALUES (%s, %s, %s)"
        for treatment in treatments:
            values = (treatment.treatmentID, treatment.treatmentDesc, treatment.treatmentCost)
            self.c.execute(querry, values)
        self.db.commit()
    
    def insert_history(self, doctor: DentistModel, patient: IdentityModel, treatments: []) -> None:
        querry = "INSERT INTO behandelgeschiedenis (patientID, dentistID, treatmentDate, behandelID) VALUES (%s, %s, %s, %s)"
        for treatment in treatments:
            values = (patient.ID, doctor.dentistID, treatment.treatmentDate, treatment.treatmentID)
            self.c.execute(querry, values)
        self.db.commit()
    
    def insert_dentists(self, dentist: DentistModel) -> None:
        querry = "INSERT INTO tandartsen (dentistID, dentistFirstName, dentistMiddleName, dentistLastName, specialty, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (dentist.dentistID, dentist.firstName, dentist.middleName, dentist.lastName, dentist.specialty, dentist.salary)
        self.c.execute(querry, values)
        self.db.commit()