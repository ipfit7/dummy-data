from models.dentist_model import DentistModel
from models.identity_model import IdentityModel
from factories.identity_factory import IdentityFactory
from util.singleton import Singleton
from random import choice

class DentistFactory(IdentityFactory):

    def create_dentist(self):
        id_fact = IdentityFactory().get_random_identity()
        dent_model = DentistModel()
        
        dent_model.address = id_fact.address
        dent_model.firstName = id_fact.firstName
        dent_model.middleName = id_fact.middleName
        dent_model.lastName = id_fact.lastName
        dent_model.placeOfResidence = id_fact.placeOfResidence
        dent_model.dateOfBirth = id_fact.dateOfBirth
        dent_model.bsn = id_fact.bsn


        return dent_model

