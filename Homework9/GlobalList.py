# შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს
#
# რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვ


int_list = [10,20,30,40]

def add_number_to_list(number):
    int_list.append(number)

add_number_to_list(50)
print(int_list)