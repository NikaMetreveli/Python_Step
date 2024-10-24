# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და
#
# დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან
#
# 1+2+3+4+5 უდრის 15-ს)


def sum_numbers(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_numbers(number//10)

print(sum_numbers(12345))

