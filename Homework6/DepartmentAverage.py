

# შექმენით დიქტი, რომელიც ინახავს ინფორმაციას დეპარტამენტების და თანამშრომლების შესახებ,
# თითოეულ თანამშრომელს უნდა ჰქონდეს ატრიბუტები:
# სახელი, გვარი, ასაკი, ხელფასი. გამოთვალეთ საშუალო ხელფასი დეპარტამენტების მიხედვით.



departments = {}

while True:
    first_name = input("Enter the employees first name(or type 'stop'): ")
    if first_name.lower() == "stop":
        break
    last_name = input("Enter the employees last name: ")
    age = int(input("Enter the employees age: "))
    salary = int(input("Enter the employees salary: "))
    department = input("Enter the employees department: ")

    employee = {
        "firstName": first_name,
        "lastName": last_name,
        "age": age,
        "salary": salary,
        "department": department.capitalize()
    }

    if department in departments:
        departments[department]["totalSalary"] += salary
        departments[department]["employeeCount"] += 1
    else:
        departments[department] = {"totalSalary": salary, "employeeCount": 1}

for dep, i in departments.items():
    averageSalary = i["totalSalary"] / i["employeeCount"]
    print(f"Average salary in {dep} is: {averageSalary}")


