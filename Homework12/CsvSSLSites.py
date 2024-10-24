# გამოიყენეთ organizations-100.csv
#
#
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი,
# ვებ საიტი, ინდუსტრია და დასაქმებულების რაოდენობა ისეთი კომპანიების რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)


import csv

with open("organizations-100.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    with open("SSLOrgs.csv", "w") as new_file:

        header = ["Organization Id", "Name", "Website", "Industry", "Number of employees"]
        writer = csv.DictWriter(new_file, fieldnames=header, extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            if "https" in row["Website"]:
                writer.writerow(row)
