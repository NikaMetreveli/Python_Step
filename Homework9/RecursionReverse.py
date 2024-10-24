# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და
#
# დააბრუნებს მის შებრუნებულ (revers) სტრიქონს ( მაგალითად input:Hello Output: olleH)
#
#
#
#


def reverse_string(word):
    if len(word) == 1:
        return word
    else:
        return reverse_string(word[1:]) + word[0]

print(reverse_string('Hello'))