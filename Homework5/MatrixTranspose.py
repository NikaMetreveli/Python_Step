# დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, ტრანსპონირება ნიშნავს ინდექსების შებრუნებას,
# მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3], ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე
#
# მაგ: [1, 2, 3]
#
# [4, 5, 6]
#
# [7, 8, 9]
#
# ტრანსპონირებული: [1, 4, 7]
#
# [2, 5, 8]
#
# [3, 6, 9]

firstMatrix = [[1,2,3],[4,5,6],[7,8,9]]

transposedMatrix = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(firstMatrix)):
    for j in range(len(firstMatrix[i])):
        transposedMatrix[j][i] = firstMatrix[i][j]

for lst in range(len(firstMatrix)):
    print(transposedMatrix[lst])