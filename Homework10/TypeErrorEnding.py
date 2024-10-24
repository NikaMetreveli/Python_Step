# დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს(ending).
# დააბრუნეთ მხოლოდ ის სიის ელემენტები, რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError)
#
# params: ['hello', 'world', 'coding', 'nod'], 'ing'
#
# outputs: ['coding']


word_list = ['hello', 'world', 'coding', 'nod']

ending_string = input("Enter your desired ending: ")

def filter_ending(given_list, ending):
    try:
        ending_filter = filter(lambda a: a[-len(ending):] == ending, given_list)
        return list(ending_filter)
    except TypeError:
        print("Only a list is permitted")

print(filter_ending(word_list, ending_string))