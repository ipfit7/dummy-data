from models.identity_model import IdentityModel
from random import choice


class EmailModel:
    _email_domains = ["aol.com"]
    email_to: str
    email_from: str
    email_cc: str
    subject: str
    content: str

    def set_to_from_identymodel(self, model: IdentityModel):
        self.email_to = "{0}@{1}".format("".join([x for x in model.full_name if x != " "]), choice(self._email_domains))
    
    def set_from_from_identymodel(self, model: IdentityModel, is_medewerker: bool = False):
        if is_medewerker:
            self.email_from = "{0}@kiesmondzorg.nl".format("".join([x for x in model.full_name if x != " "]))
        else:
            self.email_from = self.email_from = "{0}@{1}".format("".join([x for x in model.full_name if x != " "]), choice(self._email_domains))
