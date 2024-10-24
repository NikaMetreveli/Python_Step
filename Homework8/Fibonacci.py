

fibonacci_number = int(input("Enter a number: "))


def count_fibonacci(n):
    number1 = 0
    number2 = 1
    print(number1, end=" ")
    print(number2, end=" ")
    next_number = number1 + number2

    for i in range(n-3):
        print(next_number, end=" ")
        number1 = number2
        number2 = next_number
        next_number = number1 + number2

    return next_number

fibonacci_sequence = count_fibonacci(fibonacci_number)

print(fibonacci_sequence)