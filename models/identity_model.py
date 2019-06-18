import datetime

class IdentityModel:
    firstName: str
    middleName: str
    lastName: str
    bsn: str
    dateOfBirth: datetime.date
    address: str
    placeOfResidence: str

    @property
    def full_name(self) -> str:
        if len(self.middleName) > 0:
            return "{0} {1} {2}".format(self.firstName, self.middleName, self.lastName)

        return "{0} {1}".format(self.firstName, self.lastName)

    def __str__(self):
        return \
            "First name: {0}\n" \
            "Last Name: {1}\n" \
            "Middle name: {2}\n" \
            "bsn: {3}\n" \
            "date of birth: {4}\n" \
            "address: {5}\n" \
            "place of residence {6}".format(
                self.firstName,
                self.lastName,
                self.middleName,
                self.bsn,
                self.dateOfBirth,
                self.address,
                self.placeOfResidence
            )