class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_value(self):
        return sum(p.price * p.quantity for p in self.products)

    def show_inventory(self):
        for p in self.products:
            print(p.name, p.price, p.quantity)
    def get_product_list(self):
        return self.products
    def find_product(self, name):
        self.product_name = self.products
        products = [
            {'name': 'Футболка', 'quantity': 500, 'price': 10},
            {'name': 'Джинсы', 'quantity': 1000, 'price': 15},
            {'name': 'Шорты', 'quantity': 700, 'price': 20}
        ]

    def update_quantity(self, param, param1):
        pass


inventory = Inventory()

inventory.get_product_list()
inventory.show_inventory()

