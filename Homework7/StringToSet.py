# მომხმარებელს მოთხოვეთ შეიყვანოს სტრინგის ტიპის მონაცემი, დააბრუნეთ სეტი, რომლის ელემენტებიც არის სტრინგში არსებული თითოეული სიმბოლო





text = input("Enter your text: ")
charSet = set()

for i in range(0, len(text)):
    charSet.add(text[i])


print(sorted(charSet))