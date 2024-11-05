# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით




class Functor:
    def __call__(self, number):
        if number < 0:
            error = ValueError("Please enter a positive number")
            raise error
        else:
            print(number)



my_functor = Functor()
my_functor(1)
my_functor(-14)

