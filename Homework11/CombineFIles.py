# დაწერეთ პითონის პროგრამა, რომელიც წაიკითხავს ორ ფაილს და მათ გაერთიანებულს ჩაწერს ახალ ტექსტურ ფაილში.
# გაერთიანებული ფაილი წაიკითხეთ და დაბეჭდეთ ტერმინალში.



with open("Final Combo.txt", "w") as combined_file:
    with open("Combo1.txt", "r") as combo_file1:
        with open("Combo2.txt", "r") as combo_file2:
            combined_file.write(combo_file1.read())
            combined_file.write(combo_file2.read())


combo_file = open("Final Combo.txt", "r")

for i in combo_file.readlines():
    print(i)

combo_file.close()