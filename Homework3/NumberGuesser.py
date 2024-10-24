import random
from random import randint

randomNumber = randint(0,100)
lives = 5

while lives > 0:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == randomNumber:
        print("Congratulations! You have guessed the number! It is: " + str(randomNumber))
        break
    elif guess > randomNumber:
        print("The number should be lower, you have", lives-1, "guesses left.")
        lives -=1
    elif guess < randomNumber:
        print("The number should be bigger, you have", lives-1, "guesses left.")
        lives -=1
    if lives == 0:
        print("You are out of guesses! You lose! The number was: " + str(randomNumber))
        break