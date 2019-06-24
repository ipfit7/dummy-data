from models.email_model import EmailModel
from models.identity_model import IdentityModel
from util.singleton import Singleton
import mailbox

class EmailFactory(metaclass=Singleton):

    def create_email(self, sender: IdentityModel, recipient: IdentityModel, subject, content):
        model = EmailModel()
        model.set_to_from_identymodel(sender)
        model.set_from_from_identymodel(recipient)
        