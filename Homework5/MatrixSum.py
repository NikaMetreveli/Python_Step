# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს,
# ჯამი გამოითვლება შემდეგი წესით, ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს,
# მატრიცების განზომილებები უნდა იყოს ერთი და იგივე

matrix1 = [[1,2,3], [4,5,6]]
matrix2 = [[4,7,8], [12,54,34]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        sum = matrix1[i][j] + matrix2[i][j]
        print(f"Sum of row {i} and column {j} is {sum}")