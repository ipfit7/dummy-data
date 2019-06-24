from models.email_model import EmailModel
from models.identity_model import IdentityModel
from models.treatment_model import TreatmentModel
from factories.identity_factory import IdentityFactory
from util.singleton import Singleton
from datetime import datetime
import mailbox

class EmailFactory(metaclass=Singleton):

    def create_email_from_treatment(self, sender: IdentityModel, recipient: IdentityModel, treatment: TreatmentModel):
        appointment_date = IdentityFactory.random_date(datetime(day=1, month=1, year=1991), datetime(day=1, month=1, year=2020))
        model = EmailModel()
        model.set_to_from_identymodel(recipient)
        model.set_from_from_identymodel(sender, True)
        model.subject = "Uw behandeling {0} op {1} ".format(treatment.treatmentDesc, appointment_date)
        model.content = "Beste {0},\n\nUw behandeling {1} op {2} staat in de planning.\n\nMet vriendelijke groet,\n\nKiesMondzorg".format(
            recipient.lastName, treatment.treatmentDesc, appointment_date)
        return model
