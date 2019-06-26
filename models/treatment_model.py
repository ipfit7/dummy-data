from models.identity_model import IdentityModel
from datetime import datetime

class TreatmentModel:
    treatmentDesc: str
    treatmentID: int
    treatmentCost: float
    treatmentDate: datetime

    def __init__(self, cost: float, desc: str, ID: int, date: datetime):
        self.treatmentCost = cost
        self.treatmentDesc = desc
        self.treatmentID = ID
        self.treatmentDate = date
