# Task_1

def is_admin(func):
    def wrapper(*args):
        if str(*args).lower() == "admin":
            return func(*args)
        else:
            raise ValueError
    return wrapper

@is_admin
def show_customer_receipt(user_type: str) -> None:
    print("Here is your receipt")


show_customer_receipt("admin")
show_customer_receipt("user")

# Task_2

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper


@catch_errors
def number_division(number_1: int, number_2: int) -> int:
    return print(number_1 / number_2)


number_division(20, "0")

