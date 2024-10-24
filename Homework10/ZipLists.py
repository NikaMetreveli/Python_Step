# დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი და იგივე ზომის სიას(list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები ერთმანეთთან.
#
# params: [1, 2, 3], ['a', 'b', 'c']
#
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

number_list= [1,2,3]
letter_list =['a','b','c']

def zip_lists(list1, list2):
    zipped_list = zip(list1, list2)

    return list(zipped_list)

print(zip_lists(number_list, letter_list))