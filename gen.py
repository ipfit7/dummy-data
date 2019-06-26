from factories.doc_factory import DocFactory
from factories.identity_factory import IdentityFactory
from models.identity_model import IdentityModel
from factories.email_factory import EmailFactory
from models.email_model import EmailModel
from models.treatment_model import TreatmentModel
from repositories.treatment_repository import TreatmentRepository
from repositories.photo_repository import PhotoRepository
import random
import mailbox
from pathlib import Path

def create_mailbox(email: EmailModel) -> None:
    mbox = mailbox.mbox("mailbox.mbox")
    mbox.lock()
    try:
        msg = mailbox.mboxMessage()
        msg.set_unixfrom('author Sat Feb  7 01:05:34 2009')
        msg['From'] = email.email_from
        msg['To'] = email.email_to
        msg['Subject'] = email.subject
        msg.set_payload(email.content)
        mbox.add(msg)
        mbox.flush()
    finally:
        mbox.unlock()

if __name__ == "__main__":
    identity_factory = IdentityFactory()
    treatment_repo = TreatmentRepository()
    doc_factory = DocFactory()
    email_factory = EmailFactory()
    treatment_repos = TreatmentRepository()
    patients = [identity_factory.get_random_identity() for x in range(0, 50)]
    doctors = [identity_factory.get_random_identity() for y in range(0,130)]
    
    for patient in patients:
        doctor = random.choice(patients)
        treatments = [treatment_repo.get_random_treatment() for n in range(0, random.randint(0, 21))]
        doc_factory.create_doc(patient, treatments).save('dossier {0}.docx'.format(patient.bsn))
        for treatment in treatments:
            create_mailbox(email_factory.create_email_from_treatment(doctor, patient, treatment))
