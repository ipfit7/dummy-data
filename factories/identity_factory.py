from util.singleton import Singleton
from util.file_utils import get_lines_from_file
from models.identity_model import IdentityModel
from pathlib import Path
from random import randint, choice, getrandbits, randrange
from datetime import timedelta, datetime, date

class IdentityFactory(metaclass=Singleton):

    def __init__(self):

        # Static 'config' options
        self.min_date_of_birth = datetime(day=1, month=1, year=1910)
        self.max_date_of_birth = datetime(day=1, month=1, year=2015)

        # Input data
        random_names_path = Path(Path(__file__).parent.parent.joinpath("random-name"))

        self.first_names = get_lines_from_file(str(random_names_path.joinpath("first-names.txt")))
        self.middle_names = get_lines_from_file(str(random_names_path.joinpath("middle-names.txt")))
        self.last_names = get_lines_from_file(str(random_names_path.joinpath("names.txt")))

    @staticmethod
    def random_date(start: datetime, end: datetime) -> date:
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)

        return (start + timedelta(seconds=random_second)).date()

    def get_random_identity(self) -> IdentityModel:

        model = IdentityModel()

        model.address = "placeholderstreet 99"
        model.placeOfResidence = "placeholdercity"
        model.dateOfBirth = self.random_date(self.min_date_of_birth, self.max_date_of_birth)
        model.bsn = randint(100000000, 999999999)
        model.firstName = choice(self.first_names)
        model.lastName = choice(self.last_names)

        # Randomly give people middle names
        if bool(getrandbits(1)):
            model.middleName = choice(self.middle_names)
        else:
            model.middleName = ""



        return model

if __name__ == "__main__":
    factory = IdentityFactory()

    print(factory.get_random_identity())
    print(factory.get_random_identity())
    print(factory.get_random_identity())
