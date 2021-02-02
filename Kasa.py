from Products import products
prod = products()
prod.add("Питка", 100)
prod.add("Домат", 100)
prod.add("Зеле", 100)
prod.add("Лук", 10)
prod.add("Шиш", 5)
prod.add("Сос", 20)
prod.add("Тесто", 100)
prod.add("Салам", 30)
prod.add("Кашкавал", 100)
prod.add("Картофи", 95)


class kasa:
    def __init__(self):
        self.money = 1000
        self.change = 0
        self.product_use = 1
        self.bill = 0
        self.eho = []
        self.drinks_belejka = []

    def prices(self):
        print("=====================================\nДюнери:\n=====================================")
        print(f"Малък: {prod.kebap['Малък']}лв. \nСреден: {prod.kebap['Среден']}лв. \nГолям: {prod.kebap['Голям']}лв.")
        print("=====================================\nПици:\n=====================================")
        print(f"Малка: {prod.piza['Малка']}лв. \nСредна: {prod.piza['Средна']}лв. \nГоляма: {prod.piza['Голяма']}лв.")
        print("=====================================\nНапитки:\n=====================================")
        print(f"Айрян: {prod.drinks['Айрян']}лв. \nКола: {prod.drinks['Пепси']}лв.\n=====================================\n\n")

    def order(self, what, size, how_much, exception, drink):
        self.what = what
        self.size = size
        self.how_much = how_much
        self.exception = exception
        self.drink = drink
        self.bill_kebap = 0
        self.bill_pizza = 0

        if self.what == "Пица":
            if self.size == "Средна":
                self.product_use = 1.5
            elif self.size == "Голяма":
                self.product_use = 2
            prod.products["Домат"] = prod.products["Домат"] - (0.5 * self.product_use)
            prod.products["Кашкавал"] = prod.products["Кашкавал"] - (0.9 * self.product_use)
            prod.products["Салам"] = prod.products["Салам"] - (0.6 * self.product_use)
            prod.products["Тесто"] = prod.products["Тесто"] - (0.3 * self.product_use)
            if self.exception == "Салам":
                prod.products["Салам"] = prod.products["Салам"] + (0.6 * self.product_use)
            elif self.exception == "Кашкавал":
                prod.products["Кашкавал"] = prod.products["Кашкавал"] + (0.9 * self.product_use)
            elif self.exception == "Домат":
                prod.products["Домат"] = prod.products["Домат"] + (0.5 * self.product_use)
            if drink == "Айрян" or drink == "Пепси":
                self.bill_pizza = round(prod.piza[self.size] * self.how_much + prod.drinks[self.drink], 2)
                self.drinks_belejka.append(f"{self.drink}                          {prod.drinks[self.drink]}лв.")
            else:
                self.bill_pizza = prod.piza[self.size] * self.how_much
            if self.exception == "Салам" or self.exception == "Кашкавал" or self.exception == "Домат":
                self.eho.append(f"{self.what}       {self.size}      {self.how_much}     {self.bill_pizza - prod.drinks[self.drink]:.2f}лв. \n(Exception: {self.exception})")
            else:
                self.eho.append(f"{self.what}       {self.size}      {self.how_much}     {self.bill_pizza - prod.drinks[self.drink]:.2f}лв. ")

        elif self.what == "Дюнер":
            prod.products["Домат"] = prod.products["Домат"] - (0.5 * self.product_use)
            prod.products["Зеле"] = prod.products["Зеле"] - (0.3 * self.product_use)
            prod.products["Лук"] = prod.products["Лук"] - (0.1 * self.product_use)
            prod.products["Сос"] = prod.products["Сос"] - (0.3 * self.product_use)
            prod.products["Картофи"] = prod.products["Картофи"] - (0.4 * self.product_use)
            if self.exception == "Зеле":
                prod.products["Зеле"] = prod.products["Зеле"] + (0.3 * self.product_use)
            elif self.exception == "Лук":
                prod.products["Лук"] = prod.products["Лук"] + (0.1 * self.product_use)
            elif self.exception == "Домат":
                prod.products["Домат"] = prod.products["Домат"] + (0.5 * self.product_use)
            elif self.exception == "Сос":
                prod.products["Сос"] = prod.products["Сос"] + (0.3 * self.product_use)
            elif self.exception == "Картофи":
                prod.products["Картофи"] = prod.products["Картофи"] + (0.4 * self.product_use)
            if drink == "Айрян" or drink == "Пепси":
                self.bill_kebap = prod.kebap[self.size] * self.how_much + prod.drinks[self.drink]
                self.drinks_belejka.append(f"{self.drink}                          {prod.drinks[self.drink]}лв.")
            else:
                self.bill_kebap = prod.kebap[self.size] * self.how_much
            if self.exception == "Домат" or self.exception == "Зеле" or self.exception == "Лук" or self.exception == "Сос" or self.exception == "Картофи" :
                self.eho.append(f"{self.what}       {self.size}      {self.how_much}     {self.bill_kebap - prod.drinks[self.drink]:.2f}лв. \n(Exception: {self.exception})")
            else:
                self.eho.append(f"{self.what}       {self.size}      {self.how_much}     {self.bill_kebap - prod.drinks[self.drink]:.2f}лв. ")
        self.bill += self.bill_kebap + self.bill_pizza
        self.money = self.money + (self.bill_kebap + self.bill_pizza)

    def pay(self, cash):
        self.cash = cash
        self.change = round(self.cash - self.bill, 2)

    def kasova_belejka(self):
        if self.cash >= self.bill:
            print("Продукт    Размер   Брой       Цена\n____________________________________")
            for i in self.eho:
                print(i)
            print("_____________________________________\nНапитки:\n_____________________________________")
            for j in self.drinks_belejka:
                print(j)
            print(f"=====================================\n                        Общо: {self.bill}лв.")
            print(f"_____________________________________\n                         В брой: {self.cash}лв.")
            print(f"                        Ресто: {self.change}лв.")
            self.bill = 0
            self.eho = []
            self.drinks_belejka = []
        else:
            print("")

    def show_products_after(self):
        print("Продукти след поръчката:")
        for keys, value in prod.products.items():
            print(f"{keys}: {value:.2f}")

    def show_products_before(self):
        print("Продукти преди поръчката:")
        for keys, value in prod.products.items():
            print(f"{keys}: {value:.2f}")
