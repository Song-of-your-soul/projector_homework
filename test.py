class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        if speed < 0:
            raise ValueError("Speed can't be less than 0")

    @property
    def accelerate(self):
        self.speed += 5
        

    @property
    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def display_speed(self):
        return f"This is {self.brand}, {self.model}. It was made in {self.year} and it's speed is {self.speed} km\\h"


zaz = Car("ZAZ", "Slavuta", 1996, 4)
print(zaz.display_speed())
zaz.brake
print(zaz.display_speed())
