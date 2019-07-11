from models.identity_model import IdentityModel
from random import choice
from random import randint

class DentistModel(IdentityModel):
    _specialties = [
        "Orthodontist", "Mondhygienist", "Kaakchirurg", "Kaakchirurg",
        "Parodontoloog", "Endodontloog", "Gnatholoog",
        "Tandarts-dormoloog", "Angsttandarts en gehandicaptenzorg",
        "Kindertandarts-pedodontoloog", "Implantoloog",
        "Ouderentandarts (geriatrie-tandarts)", "Restauratief tandarts",
        "Biologische tandarts", "Botox specialist type I", "Botox specialist type II"
        ]
    _salraries = [
        2000.00, 2500.00, 3000.00, 3500.00, 4000.00, 2750.00, 2250.00
    ]
    specialty = ""
    salary = 0.0
    dentistID = 0

    def __init__(self):
        self.specialty = choice(self._specialties)
        self.salary = choice(self._salraries)
        self.dentistID = randint(1000, 9999)

        super().__init__()
   