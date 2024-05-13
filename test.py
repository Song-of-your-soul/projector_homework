menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15},
}

dish_name = "burger"


if dish_name not in menu:
    print("No such position")
else:
    print(menu[dish_name]["quantity"])
