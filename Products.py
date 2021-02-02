class products:
    def __init__(self):
        self.products = {}
        self.drinks = {"Айрян": 0.49, "Пепси": 1.29}
        self.piza = {"Малка": 2.49, "Средна": 3.49, "Голяма": 5}
        self.kebap = {"Малък": 3, "Среден": 4, "Голям": 5}

    def add(self, product, amount):
        self.prod = product
        self.amount = amount
        self.products[self.prod] = self.amount
