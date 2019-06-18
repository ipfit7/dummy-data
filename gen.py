from docx import Document
import random

def main():
    create_doc()

def create_doc(nr, naam):
    #create document
    document = Document()
    document.add_heading('Patient Dossier van ' + naam, 0)
    patientInfo = document.add_table(rows=5, cols=2)
    desc_cells = patientInfo.columns[0].cells
    desc_cells[0].text = "Patient nummer"
    desc_cells[1].text = "Naam"
    desc_cells[2].text = "Geboorte datum"
    desc_cells[3].text = "Woonplaats"
    desc_cells[4].text = "BSN"
    info_cells = patientInfo.columns[1].cells
    # info_cells[0].text = nr 
    # info_cells[1].text = naam
    # info_cells[2].text = datum
    # info_cells[3].text = plaats
    desc_cells[4].text = random.randint(100000000, 3000000000)
    document.add_heading("Behandelingen" level=1)
    behandelingen = document.add_table(rows=4, cols=2)
    document.save('test.docx')


def data_gen():
    #random name generator
    data = {}
    aantal = 0
    with open('dummy-data/random-name/first-names.txt', 'r') as voornamenlijst:
        for naam in voornamenlijst:
            data.update{unit : {voornaam : naam}}

if __name__ == "__main__":
    main()