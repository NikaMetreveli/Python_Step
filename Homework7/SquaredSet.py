
# შექმენით ცვლადი squared_numbers რომელიც შეიცავს 1-დან 10-ის ჩათვლით კვადრატში აყვანილ რიცხვებს(არ შეავსოთ ხელით, გამოიყენეთ სეტის ტიპის მონაცემი)


squaredNumbers = set()

for i in range(1,11):

    squaredNumber = i**2
    squaredNumbers.add(squaredNumber)


print(sorted(squaredNumbers))