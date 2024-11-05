# დაწერეთ დეკორატორი, რომელიც გამოთვლის ფუნქციის მოქმედების დროს და დაბეჭდავს ტერმინალში. დროის აღსაქმელად გამოიყენეთ time.time()

import time

def decorator(func):
    def wrapper(number):
        start_time = time.time()
        if number < 0:
            error = ValueError("Please enter a positive number.")
            raise error
        else:
            func(number)
        end_time = time.time()
        print(f"The function took {end_time - start_time} seconds to run")

    return wrapper



@decorator
def print_number(number):
    for i in range(number):
        print(i, end= "\n")

input_number = int(input("Enter a number: "))
print_number(input_number)