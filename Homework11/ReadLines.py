# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მასში ჩაწერს 1000 ხაზს(ტექსტს არ აქვს მნიშვნელობა) თავისი ნუმერაციით,
# შემდეგ წაიკითხეთ ეს ფაილი და დაბეჭდეთ ხაზების რაოდენობა, თუ რამდენია შევსებული.




with open("text.txt", "w") as text_file:
    for i in range(1000):
        text_file.write(str(i) + "\n")


with open("text.txt", "r") as read_file:
    line_count = len((read_file.readlines()))
    print(f"There are {line_count} lines in the file")

