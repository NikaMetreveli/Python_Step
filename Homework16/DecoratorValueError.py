# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი,
# რომელიც შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი, თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით,
# სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან.



def decorator(func):
    def wrapper(number):
        if number < 0:
            error = ValueError("Please enter a positive number.")
            raise error
        else:
            func(number)
    return wrapper

@decorator
def print_number(number):
    print(number)

print_number(1)
print_number(-14)