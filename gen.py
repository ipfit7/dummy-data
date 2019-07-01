from factories.doc_factory import DocFactory
from factories.identity_factory import IdentityFactory
from factories.dentist_factory import DentistFactory
from factories.books_factory import BookFactory
from models.identity_model import IdentityModel
from factories.email_factory import EmailFactory
from models.email_model import EmailModel
from models.treatment_model import TreatmentModel
from repositories.treatment_repository import TreatmentRepository
from repositories.photo_repository import PhotoRepository
from repositories.sql_repository import SQLRepository
import random
import mailbox
from pathlib import Path

if __name__ == "__main__":
    identity_factory = IdentityFactory()
    treatment_repo = TreatmentRepository()
    sql_repo = SQLRepository()
    doc_factory = DocFactory()
    email_factory = EmailFactory()
    treatment_repos = TreatmentRepository()
    dentist_factory = DentistFactory()
    books_factory = BookFactory()
    Path.mkdir("./data", exist_ok=True)
    Path.mkdir("./data/mail", exist_ok=True)
    Path.mkdir("./data/patient_dossiers", exist_ok=True)
    patients = [identity_factory.get_random_identity() for x in range(0, 50)]
    doctors = [dentist_factory.create_dentist() for y in range(0,30)]
    sql_repo.insert_treatments(treatment_repo.get_treatment(n) for n in range(10,23))
    books_factory.make_tables()

    for doctor in doctors:
        sql_repo.insert_dentists(doctor)
    
    for patient in patients:
        doctor = random.choice(doctors)
        sql_repo.insert_patients(patient)
        treatments = [treatment_repo.get_random_treatment() for n in range(0, random.randint(0, 21))]
        doc_factory.create_doc(patient, treatments).save('./data/patient_dossiers/dossier {0}.docx'.format(patient.ID))
        sql_repo.insert_history(doctor, patient, treatments)
        books_factory.make_books(treatments)
        for treatment in treatments:
            email_factory.create_mailbox(email_factory.create_email_from_treatment(doctor, patient, treatment), treatment)
