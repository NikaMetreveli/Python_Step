# list comprehension გამოყენებით შექმენით რენდომ რიცხვებისგან შემდგარი 4x4 კვადრატული მატრიცა


import random

randomList = []

for i in range(16):
    number = random.randint(1, 100)
    randomList.append(number)

print(randomList)

matrix = [randomList[i:i+4] for i in range(0,16,4)]

print(matrix)

