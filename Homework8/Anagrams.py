

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

def is_anagram(text1, text2):
    word1_sorted = sorted(text1)
    word2_sorted = sorted(text2)
    if word1_sorted == word2_sorted:
        print(f"The words: {text1} and {text2} are anagrams")
    else:
        print(f"The words: {text1} and {text2} are not anagrams")


is_anagram(word1, word2)