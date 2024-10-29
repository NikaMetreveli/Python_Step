# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები.
# შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცი


class BankAccount:

    def __init__(self, account_number, account_owner, balance):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance

    def check_balance(self):
        print(f"Balance on account number '{self.account_number}' is {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds on {self.account_owner}'s balance")
        else:
            new_balance = self.balance - amount
            print(f"{amount} was withdrawn from {self.account_owner}'s balance, new balance is {new_balance}")
            self.balance = new_balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        print(f"{amount} was deposited onto {self.account_owner}'s balance, new balance is {new_balance}")
        self.balance = new_balance


account1 = BankAccount("1", "Nikolozi", 10000)
account2 = BankAccount("2", "Giorgi", 20000)

account1.withdraw(2000)

account1.check_balance()

account2.deposit(2000)

account1.deposit(1234)

account2.withdraw(30000)

account2.check_balance()

account1.check_balance()