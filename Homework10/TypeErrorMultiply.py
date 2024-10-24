# დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს,
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
#
# params:[1, 2, 3, 4, 5]
#
# output: 120
import functools

list1 = [1,2,3,4,5]

def list_multiplication(given_list):
    try:
        multiplied_list = functools.reduce(lambda x,y : x*y, given_list)
        return multiplied_list
    except TypeError:
        print("Wrong input, you can only enter a list")

print(list_multiplication(list1))