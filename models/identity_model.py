import datetime

class IdentityModel:
    ID = ""
    firstName = ""
    middleName = ""
    lastName = ""
    bsn = ""
    dateOfBirth = None
    address = ""
    placeOfResidence = ""

    @property
    def full_name(self) -> str:
        if len(self.middleName) > 0:
            return "{0} {1} {2}".format(self.firstName, self.middleName, self.lastName)

        return "{0} {1}".format(self.firstName, self.lastName)

    def __str__(self):
        return \
            "ID: {0}\n" \
            "First name: {1}\n" \
            "Last Name: {2}\n" \
            "Middle name: {3}\n" \
            "bsn: {4}\n" \
            "date of birth: {5}\n" \
            "address: {6}\n" \
            "place of residence {7}".format(
                self.ID,
                self.firstName,
                self.lastName,
                self.middleName,
                self.bsn,
                self.dateOfBirth,
                self.address,
                self.placeOfResidence
            )