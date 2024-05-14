# Task_1


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, price: int, quantity: int, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(
            f"This is {self.name}, written by {self.author}. Its price is {self.price}. {self.quantity} books were published"
        )


book = Book("451 Fahrenheit", 25, 10_000_000, "Ray Douglas Bradbury")
book.read()

# Task_2


class Restaurant:
    def __init__(self, name: str, quisine: str, menu: dict):
        self.name = name
        self.quisine = quisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, quisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, quisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name: str, quantity: int):
        if dish_name not in self.menu:
            print(f"There is no such position as {dish_name} in our menu")
        elif quantity > self.menu[dish_name]["quantity"]:
            print(
                f"Unfortunately we don't have {quantity} portions of {dish_name} in our menu"
            )
        else:
            order_price = self.menu[dish_name]["price"] * quantity
            answer = input(
                f"The total cost of your order is {order_price}, do you want to proceed with payment?"
            )
            if answer.lower() == "yes":
                self.menu[dish_name]["quantity"] -= quantity
                return order_price
            else:
                print(
                    "Thank you for your time. If you still want to make an order, try one more time"
                )


menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15},
}


mcdonalds = FastFood("McDonald's", "International", menu, True)
print(mcdonalds.menu)
mcdonalds.order("pizza", 10)
print(mcdonalds.menu)

# Task_3


class Account:
    def __init__(self, balance: int, account_number: int):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account number: {self._account_number}, balance: {self._balance}"


class SavingsAccount(Account):
    def __init__(self, balance: int, account_number: int, interest: int):
        super().__init__(balance, account_number)
        self.interest = interest

    def gain_interest(self):
        self._balance += self.interest


class CurrentAccount(Account):
    def __init__(self, balance: int, account_number: int, overdraft_limit: int):
        super().__init__(balance, account_number)
        self.limit = overdraft_limit


class Bank:
    def __init__(self, accounts: list):
        self.accounts = accounts

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.gain_interest()
            elif isinstance(account, CurrentAccount):
                if account.limit > account._balance:
                    print(
                        f"Hello! Unfortunately account {account._account_number} in overdraft. Please, top up the account!"
                    )

    def open_account(self, account_number: int):
        self.accounts.append(Account.create_account(account_number))

    def close_account(self, name: str):
        if name in self.accounts:
            self.accounts.remove(name)

    def dividends(self, money: int):
        for account in self.accounts:
            account._balance += money


good_account = SavingsAccount(1000, 80991489, 200)
bad_account = CurrentAccount(300, 80971487, 500)
okay_account = SavingsAccount(500, 81001500, 200)
just_okay_account = CurrentAccount(700, 80000000, 500)

accounts = [good_account, bad_account, okay_account, just_okay_account]

Hello_bank = Bank(accounts)
Hello_bank.update()
for account in Hello_bank.accounts:
    print(account)
Hello_bank.close_account(okay_account)
Hello_bank.open_account(10101010)
Hello_bank.dividends(1000)
print("New balances: ")
for account in Hello_bank.accounts:
    print(account)