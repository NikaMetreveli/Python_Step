# გამოიყენეთ organizations-100.csv
#
#
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “sorted_csv.csv” და ჩაწერეთ დასორტირებული ინფორმაცია, დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით


import csv


with open("organizations-100.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    with open("sorted_orgs.csv", "w") as sorted_file:
        sorted_list = sorted(reader, key=lambda k: int(k['Number of employees']))
        header = ["Index", "Organization Id", "Name", "Website", "Country", "Description", "Founded", "Industry", "Number of employees"]
        writer = csv.DictWriter(sorted_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(sorted_list)
