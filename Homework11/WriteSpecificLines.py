# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მეორე, მერვე,
# მეათე, მეცამეტე და მეჩვიდმეტე ხაზებზე ჩაწერს ამ რიცხვებს შესაბამისი ტექსტური სახელით.



with open("text1.txt", "w") as text_file:
    for i in range(20):
        if i == 1 or i == 9 or i == 11 or i == 14 or i == 18:
            text_file.write("" + str(i+1) + "\n")
        else:
            text_file.write("\n")

