from models.email_model import EmailModel
from models.identity_model import IdentityModel
from models.treatment_model import TreatmentModel
from factories.identity_factory import IdentityFactory
from util.singleton import Singleton
from datetime import datetime, timedelta
import mailbox
import time

class EmailFactory(metaclass=Singleton):

    def create_email_from_treatment(self, sender: IdentityModel, recipient: IdentityModel, treatment: TreatmentModel):
        appointment_date = treatment.treatmentDate
        model = EmailModel()
        model.set_to_from_identymodel(recipient)
        model.set_from_from_identymodel(sender, True)
        model.subject = "Uw behandeling {0} op {1} ".format(treatment.treatmentDesc, appointment_date)
        model.content = "Beste {0},\n\nUw behandeling {1} op {2} staat in de planning.\n\nMet vriendelijke groet,\n\nKiesMondzorg".format(
            recipient.lastName, treatment.treatmentDesc, appointment_date)
        return model
    
    def create_mailbox(self, email: EmailModel, app_date: TreatmentModel) -> None:
        sentdate = app_date.treatmentDate - timedelta(days=20)
        mbox = mailbox.mbox("mailbox.mbox")
        mbox.lock()
        try:
            msg = mailbox.mboxMessage()
            msg.set_unixfrom('author Sat Feb  7 01:05:34 2009')
            msg.set_from("MAILER DAEMON", time.strptime(str(sentdate) + " 12:00", "%Y-%m-%d %H:%M"))
            msg['From'] = email.email_from
            msg['To'] = email.email_to
            msg['Subject'] = email.subject
            msg.set_payload(email.content)
            mbox.add(msg)
            mbox.flush()
        finally:
            mbox.unlock()
