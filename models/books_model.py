from random import choice

class BooksModel:
    income = 0.0
    expence = 0.0
    _expences = (5.00, 12.00, 10.00, 20.00, 7.50, 3.50, 15.25)
    vat = 0.0
    tax = 0.0
    quarter = 0.0

    def __init__(self):
        self.expence = choice(self._expences)
