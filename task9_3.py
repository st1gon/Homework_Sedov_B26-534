class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Book(Product):
    def __init__(self, name, price, stock, author):
        super().__init__(name, price, stock)
        self.author = author

class Electronic(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, name, quantity):
        for p in self.products:
            if p.name == name and p.stock >= quantity:
                p.stock -= quantity
                return True
        return False
