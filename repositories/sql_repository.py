from util.singleton import Singleton
from factories.identity_factory import IdentityFactory
from repositories.treatment_repository import TreatmentRepository
from models.treatment_model import TreatmentModel
from models.identity_model import IdentityModel
import MySQLdb

class SQLRepository(metaclass=Singleton):

    def __init__(self):
        self.db = MySQLdb.connect(host='127.0.0.1', user='root', database='patientinfo')
        self.c = self.db.cursor()
        self.id_factory = IdentityFactory()
        
    
    def insert_patients(self, patient: IdentityModel):
        querry = "INSERT INTO patients (firstName, middleName, lastName, bsn, dateOfBirth, address, placeOfResidence) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # identity = self.id_factory.get_random_identity()
        values = (patient.firstName, patient.middleName, patient.lastName, patient.bsn, patient.dateOfBirth, patient.address,
            patient.placeOfResidence)
        self.c.execute(querry, values)
        self.db.commit()
    
    def insert_treatments(self, treatments: []):
        querry = "INSERT INTO behandelingen (behandelID, behandelDesc, behandelCost) VALUES (%s, %s, %s)"
        for treatment in treatments:
            values = (treatment.treatmentID, treatment.treatmentDesc, treatment.treatmentCost)
            self.c.execute(querry, values)
        self.db.commit()
    
    def insert_history(self, doctor: IdentityModel, patient: IdentityModel, treatments: []):
        querry = "INSERT INTO behandelgeschiedenis (patientID, dentistID, treatmentDate, behandelID) VALUES (%s, %s, %s, %s)"
        for treatment in treatments:
            values = (patient.bsn, doctor.bsn, treatment.treatmentDate, treatment.treatmentID)
            self.c.execute(querry, values)
        self.db.commit()