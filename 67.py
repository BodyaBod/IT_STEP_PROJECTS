
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.quantity > 0:
            self.products.append(product)
            print("Товар додано!")
        else:
            print("Товару немає в наявності!")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print("Товар видалено!")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        for product in self.products:
            print(product.name, "-", product.price, "грн")
        print("Загальна сума:", self.total_price(), "грн")


phone = Product("Телефон", 5000, 3)
mouse = Product("Мишка", 500, 5)
keyboard = Product("Клавіатура", 1000, 0)

cart = Cart()

cart.add_product(phone)
cart.add_product(mouse)
cart.add_product(keyboard)

cart.show_cart()

cart.remove_product(mouse)

cart.show_cart()
