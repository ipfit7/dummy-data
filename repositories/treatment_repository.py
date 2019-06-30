from util.singleton import Singleton
from models.treatment_model import TreatmentModel
from factories.identity_factory import IdentityFactory
from datetime import datetime
from random import randint
from copy import deepcopy

class TreatmentRepository(metaclass=Singleton):

    def __init__(self):
        self._treatments = {
            10 : TreatmentModel(10.00, "Routine controle", 10, None),
            11 : TreatmentModel(30.00, "Tand of kies trekken", 11, None),
            12 : TreatmentModel(50.00, "Wortelkanaalbehandeling", 12, None),
            13 : TreatmentModel(75.00, "Facing", 13, None),
            14 : TreatmentModel(150.00, "Kunstgebit", 14, None),
            15 : TreatmentModel(80.00, "Kroon", 15, None),
            16 : TreatmentModel(65.00, "Sealen", 16, None),
            17 : TreatmentModel(175.00, "Implantaat", 17, None),
            18 : TreatmentModel(95.00, "Brug", 18, None),
            19 : TreatmentModel(50.00, "Vulling", 19, None),
            20 : TreatmentModel(60.00, "Xray", 20, None),
            21 : TreatmentModel(50.00, "Botox spuiten type I", 21, None),
            22 : TreatmentModel(65.00, "Botox spuiten type II", 22, None)
        }
    
    def get_treatment(self, treatmentID: int) -> TreatmentModel:
        return self._treatments[treatmentID]

    def get_random_treatment(self) -> TreatmentModel:
        treatment = deepcopy(self._treatments[randint(10, 22)])
        treatment.treatmentDate = IdentityFactory.random_date(datetime(day=1, month=1, year=1991), datetime(day=1, month=1, year=2020))
        return treatment
        
