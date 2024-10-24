
# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი,
# ააწყვეთ კალკულატორი, რომელიც გამოთვლის შესაბამის მოქმედებას, გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად იქნება მათემატიკური ოპერატორები

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter an operator: ")



calculatorDict = {
    "+": number1 + number2,
    "-": number1 - number2,
    "*": number1 * number2,
    "/": number1 / number2,
    "//": number1 // number2,
    "**": number1 ** number2,
    "%":number1 % number2
}

result = calculatorDict.get(operator)

print("The answer is", result)