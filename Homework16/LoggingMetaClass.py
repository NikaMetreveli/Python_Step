# შექმენით მეტაკლასი LoggingMeta, რომელიც ყოველი კლასის შექმნის დროს დაბეჭდავს თუ რა სახელის მქონე კლასი იქმნება და რა მეთოდები გააჩნია მას.


class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        print(name)
        print(dct)
        return instance


class Car(metaclass= LoggingMeta):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def return_values(self):
        return f'Brand: {self.brand}, Model: {self.model}'

    def return_brand(self):
        return f'Brand: {self.brand}'

car1 = Car('Mercedes', 'C550')
print(car1.return_values())