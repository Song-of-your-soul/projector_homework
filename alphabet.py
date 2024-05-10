# Task_1

import random

for letter in range(65, 91):
    with open(f"{chr(letter)}.txt", "w") as file:
        file.write(str(random.randint(1, 100)))


with open("summary.txt", "a") as file:
    for letter in range(65, 91):
        with open(f"{chr(letter)}.txt", "r") as file_2:
            text = file_2.read()
        file.write(f"{chr(letter)}.txt: {text}\n")
