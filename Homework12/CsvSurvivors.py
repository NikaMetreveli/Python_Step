# გამოიყენეთ titanic.csv
#
#
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “survived.csv” და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.

import csv


with open("titanic.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)


    with open("Survivors.csv", "w") as survivors_file:
        headers = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
        writer = csv.DictWriter(survivors_file, fieldnames=headers)
        writer.writeheader()
        for row in reader:
            if row["Survived"] == "1":
                writer.writerow(row)