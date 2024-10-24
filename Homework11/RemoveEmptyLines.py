# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტებად მიიღებს ფაილის სახელებს,
# წაიკითხეთ ერთი ფაილი, ამოშალეთ ცარიელი ხაზები და სრული ინფორმაცია ჩაწერეთ მეორე ფაილში.



def remove_empty_lines(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    with open("not_empty.txt", "w") as new_file:
        for i in lines:
            if i != "\n":
               new_file.write(i)



remove_empty_lines("EmptyLineFile.txt")