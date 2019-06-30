from random import choice

class BooksModel:
    income: float
    expence: float
    _expences = (5.00, 12.00, 10.00, 20.00, 7.50, 3.50, 15.25)
    vat: float
    tax: float
    quarter: str

    def __init__(self):
        self.expence = choice(self._expences)
