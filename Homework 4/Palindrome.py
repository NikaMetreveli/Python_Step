

word = input('Enter a word: ')
reversedWord = ""

for i in range(len(word)):
    letter = word[len(word)-i-1]
    reversedWord += letter


if reversedWord == word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")