

user_text = input("Enter your text: ")
user_char = input("Enter your character: ")

def count_characters(text, char):
    count = 0
    for i in range(len(text)):
        if text[i] == char:
            count += 1
        else:
            pass

    return count

answer = count_characters(user_text, user_char)
print(f"The character '{user_char}' can be found {answer} times in the word '{user_text}'")