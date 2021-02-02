from Kasa import kasa
k = kasa()


class customer:
    def __init__(self):
        self.cash = 0

    def order(self, what, size, how_much, exception, drink):
        self.what = what
        self.size = size
        self.how_much = how_much
        self.exception = exception
        self.drink = drink
        k.order(self.what, self.size, self.how_much, self.exception, self.drink)

    def pay(self, cash):
        self.cash = cash
        if self.cash >= k.bill:
            k.pay(self.cash)
        elif self.cash < k.bill:
            print(f"Парите са недостатъчни, трябват ти още: {k.bill - self.cash:.2f}лв.\n_____________________________________")

    def kasova_belejka(self):
        if self.cash >= k.bill:
            k.kasova_belejka()
