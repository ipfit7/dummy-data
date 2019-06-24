from models.identity_model import IdentityModel
from random import choice


class EmailModel:
    _email_domains = ["@gmail.com", "@yandex.ru", "@kiesmondzorg.nl", "@live.nl"]
    email_to: str
    email_from: str
    email_cc: str
    subject: str
    content: str

    def set_to_from_identymodel(self, model: IdentityModel):
        self.email_to = model.full_name + choice(self._email_domains)
    
    def set_from_from_identymodel(self, model: IdentityModel):
        self.email_from = model.full_name + choice(self._email_domains)
