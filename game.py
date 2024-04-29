import random
import csv

# Task_3


def game_played() -> list:
    players = ["Player_1", "Player_2", "Player_3", "Player_4", "Player_5"]
    highscores = []
    for player in players:
        highest_score = 0
        for _ in range(100):
            score = random.randint(0, 1000)
            if score > highest_score:
                highest_score = score
        highscores.append([player, highest_score])
    print(highscores)
    with open("best_score.csv", "w") as file:
        writer = csv.writer(file)
        for i in highscores:
            writer.writerow(i)


game_played()

# Task_4


def highscores():
    highest_scores = []
    score_numbers = []
    with open("best_score.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row != []:
                highest_scores.append(row)
        print(highest_scores)
    for player in highest_scores:
        score_numbers.append(player[1])
    score_numbers.sort(reverse=True)
    print(score_numbers)
    while highest_scores != []:
        for index, score in enumerate(highest_scores):
            if score[1] == score_numbers[0]:
                with open("high_scores.csv", "a") as file2:
                    writer = csv.writer(file2)
                    writer.writerow(score)
                    score_numbers.remove(score[1])
                    highest_scores.remove(score)
