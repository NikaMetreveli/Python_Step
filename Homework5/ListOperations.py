# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს
#
# შემდეგ ნაბიჯებს:
#
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
#
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
#
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
#
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2
#
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტები

myList = [43, '22', 12, 66, 210, ["hi"]]

#A

print(f"Index of 210 in the list is: {myList.index(210)}")

#B

myList.append("hello")
print(myList)

#C

myList.pop(2)
print(myList)

#D

myList2 = myList
myList2.clear()
print(myList)
print(myList2)
