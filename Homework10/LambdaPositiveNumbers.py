# დაწერეთ lambda ფუნქცია, რომელიც დააბრუნებს მხოლოდ რიცხვის დადებით მნიშვნელობებს,
# შესამოწმებელი რიცხვები აღწერილი უნდა იყოს ლისტში. გამოიყენეთ filter ფუნქცია functools მოდულიდან


number_list = [1, -2, 3, 104, 24, -23, 54, -34, -1000, 20]


def filter_positives(list1):

    positive_filter = filter(lambda x: x >= 0, list1)
    return list(positive_filter)

print(filter_positives(number_list))