from docx import Document
from factories.identity_factory import IdentityFactory
from models.identity_model import IdentityModel
import random


def create_doc(identity: IdentityModel) -> None:
    # Placeholder
    patient_nr = random.randint(10000, 99999)

    #create document
    document = Document()
    document.add_heading('Patient Dossier van ' + identity.full_name, 0)

    # Create table
    patientInfo = document.add_table(rows=5, cols=2)

    desc_cells = patientInfo.columns[0].cells
    desc_cells[0].text = "Patient nummer"
    desc_cells[1].text = "Naam"
    desc_cells[2].text = "Geboorte datum"
    desc_cells[3].text = "Woonplaats"
    desc_cells[4].text = "BSN"

    info_cells = patientInfo.columns[1].cells

    info_cells[0].text = str(patient_nr)
    info_cells[1].text = identity.full_name
    info_cells[2].text = str(identity.dateOfBirth)
    info_cells[3].text = identity.placeOfResidence
    info_cells[4].text = str(identity.bsn)

    document.save("dossier {0}.docx".format(patient_nr))


if __name__ == "__main__":
    factory = IdentityFactory()

    for i in range(1, 20):
        create_doc(factory.get_random_identity())
