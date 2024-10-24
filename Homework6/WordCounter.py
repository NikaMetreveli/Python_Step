

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება, პროგრამას დააბეჭდინეთ დიქტის სახით
# რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში
#
#
# input: The wind howled and howled all night long
#
# output: {“the”: 1, “wind”:1, “howled”:2, “and”:1, “all”:1, ”night”:1, “long”:1}


sentence = input("Enter a sentence: ")


resultDict = {}

wordsList = sentence.split()

for i in wordsList:
    if i in resultDict:
        resultDict[i] += 1
    else:
        resultDict[i] = 1

print(resultDict)