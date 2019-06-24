from models.identity_model import IdentityModel

class TreatmentModel:
    treatmentDesc: str
    treatmentID: int
    treatmentCost: float

    def __init__(self, cost: float, desc: str, ID: int):
        self.treatmentCost = cost
        self.treatmentDesc = desc
        self.treatmentID = ID
