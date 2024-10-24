

# შექმენით 20 რენდომ რიცხვისგან შემდგარი ლისტი, შექმენით ახალი ლისტი, რომელშიც შეინახავთ პირველი ლისტიდან მხოლოდ კენტ მნიშვნელობებს
# და დაბეჭდეთ ლისტში ყველაზე მცირე და ყველაზე დიდი ელემენტი. არ გამოიყენოთ ფუნქციები min() და max()

import random

randomList = []
evenList =[]

for i in range(20):

    randomNumber = random.randrange(0,500)

    randomList.append(randomNumber)

print(randomList)

for i in range(len(randomList)):
    if randomList[i-1] % 2 == 1:
        evenList.append(randomList[i-1])

print(f"Even numbers from the first list are: {evenList}")
evenList.sort()
print(f"The minimum value is: {evenList[0]}")
print(f"The maximum value is: {evenList[-1]}")
