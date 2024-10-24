# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს ფაილის სახელს, წაიკითხეთ ფაილი,
# დაყავით ხაზები რაოდენობის მიხედვით და ჩაწერეთ ახალ ფაილებში, თითოში მაქსიმუმ 10 ხაზი.

def divide_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)

    file_count = (line_count // 10) + (1 if line_count % 10 != 0 else 0)

    for i in range(file_count):
        start = i*10
        end = (i+1)*10
        with open("DividedFile" + str(i+1) +".txt", 'w') as new_file:
            new_file.writelines(lines[start:end])


divide_file("DivideTest.txt")