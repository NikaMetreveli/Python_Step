


import json


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product name: {self.name}, Price: {self.price}, Stock: {self.quantity}'


def custom_serializer(obj):
    if isinstance(obj, Product):
        return {
            "Name": obj.name,
            "Price": obj.price,
            "Quantity": obj.quantity
        }
    return obj

def custom_deserializer(json_data):
    return Product(json_data["Name"], json_data["Price"], json_data["Quantity"])

lst = []

product1 = Product("Iphone 16", 4000, 250)
product2 = Product("Samsung Galaxy S24 Ultra", 4500, 150)
product3 = Product("Pixel 8 Pro", 3500, 200)

lst.append(product1)
lst.append(product2)
lst.append(product3)

with open('products.json', 'w') as json_file:
    json.dump(lst, json_file, default=custom_serializer, indent=4)

with open('products.json', "r") as json_read:
    data = json.load(json_read, object_hook=custom_deserializer)

for product in data:
    print(product)