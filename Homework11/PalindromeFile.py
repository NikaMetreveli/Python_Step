# დაწერეთ ფუნქცია, რომელიც წაიკითხავს ფაილს, დაბეჭდეთ ის ხაზები,
# რომელიც არის ერთმანეთის პალინდრომი




def print_palindromes(file_name):

    with open(file_name, 'r') as file:
        lines = file.readlines()


    for i in lines:
        if i.lower().split()==i[::-1].lower().split() and i!="\n":
            print(i)


print_palindromes('palindromes.txt')