class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __str__(self):
        return f"{self.name} is a country with {self.population} people"

    def __add__(self, other_country):
        new_name = self.name + " " + other_country.name
        new_population = self.population + other_country.population
        return Country(new_name, new_population)

    def add(self, other_country):
        new_name = self.name + " " + other_country.name
        new_population = self.population + other_country.population
        return Country(new_name, new_population)


# Task_1


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina)

# Task_2

ukraine = Country("Ukraine", 37_000_000)
usa = Country("USA", 333_000_000)
ukraine_usa = ukraine + usa
print(ukraine_usa)

# Task_3


class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        if speed < 0:
            raise ValueError("Speed can't be less than 0")

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def display_speed(self):
        return f"This is {self.brand}, {self.model}. It was made in {self.year} and it's speed is {self.speed} km\\h"


zaz = Car("ZAZ", "Slavuta", 1996, 4)
print(zaz.display_speed())
zaz.accelerate()
print(zaz.display_speed())
zaz.brake()
print(zaz.display_speed())

# Task_4


class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        orientation_variants = ["left", "down", "right", "up"]
        if orientation not in orientation_variants:
            raise ValueError("No such orientation option")
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "left":
            self.position_x -= steps
        if self.orientation == "right":
            self.position_x += steps
        if self.orientation == "down":
            self.position_y -= steps
        if self.orientation == "up":
            self.position_y += steps

    def turn(self, direction):
        directions = ["left", "right"]
        rotation = ["up", "right", "down", "left"]
        if direction not in directions:
            raise ValueError("No such direction option")
        if direction == "left":
            for element, i in enumerate(rotation):
                if i == self.orientation:
                    if element != 0:
                        self.orientation = rotation[element - 1]
                    else:
                        self.orientation = rotation[-1]
        else:
            for element, i in enumerate(rotation):
                if i == self.orientation:
                    if i != rotation[-1]:
                        self.orientation = rotation[element + 1]
                    else:
                        self.orientation = rotation[0]

    def display_position(self):
        return f"This robot is located at point A({self.position_x}, {self.position_y}) of our map. It is facing {self.orientation}"


robo = Robot("left", 0, 0)
print(robo.display_position())
robo.move(5)
print(robo.display_position())
robo.turn("right")
robo.move(5)
print(robo.display_position())
