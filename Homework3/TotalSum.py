

totalSum = 0

while True:

    number = input("Enter a number: ")
    if number.lower() == "sum":
        print("Total sum of your numbers is: " + str(totalSum))
        break
    else:
        totalSum = totalSum + int(number)