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
    specialty: str
    dentistID: int

    def __init__(self):
        self.specialty = choice(self._specialties)
        self.dentistID = randint(1000, 9999)

        super().__init__()
   