
# დაწერეთ lambda ფუნქცია რომელიც იღებს სიას(list) და აბრუნებს მხოლოდ სიის ლუწ ელემენტებს
#
# params: [1, 2, 3, 4, 5, 6, 7]
#
# outputs: [2, 4, 6]


number_list = [1,2,3,4,5,6,7]


def filter_evens(list1):
    list_filter = filter(lambda x: x % 2 == 0, number_list)
    return list(list_filter)

print(filter_evens(number_list))


