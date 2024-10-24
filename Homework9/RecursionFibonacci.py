# დაწერეთ რეკურსიული ფუნქცია, დააბრუნებს ფიბონაჩის მიმდევრობას.
#
# ფიბონაჩის მიმდევრობის თანახმად ყოველი რიცხვი წინა ორი რიცხვის ჯამია
#
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21

number = input("Please enter your number: ")

def count_fibonacci(n):
    if n <= 1:
        return n
    else:
        return count_fibonacci(n-1) + count_fibonacci(n-2)

for i in range(int(number)):
    print(count_fibonacci(i), end= " ")

