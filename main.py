from Customer import customer
from Kasa import kasa
k = kasa()
k.show_products_before()
print("")
k.prices()
c = customer()
c.order("Пица", "Голяма", 3, "Домат", "Пепси")
c.order("Дюнер", "Голям", 2, "Зеле", "Айрян")
c.order("Пица", "Средна", 4, "Не", "Пепси")
c.pay(50)
c.kasova_belejka()
k.show_products_after()
print("\n Сценарий 2:\n")
c = customer()
c.order("Дюнер", "Голям", 2, "Лук", "Пепси")
c.order("Дюнер", "Малък", 1, "Не", "Айрян")
c.order("Пица", "Средна", 3, "Салам", "Пепси")
c.pay(20)
c.kasova_belejka()