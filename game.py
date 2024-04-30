import random
import csv

# Task_3


def game_played() -> list:
    players = ["Player_1", "Player_2", "Player_3", "Player_4", "Player_5"]
    highscores = []
    for player in players:
        for _ in range(100):
            score = random.randint(0, 1000)
            highscores.append([player, score])
    with open("highscores.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for i in highscores:
            writer.writerow(i)



# Task_4


def highscores():
    highest_scores = []
    score_numbers = []
    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            highest_scores.append(row)
    for player in highest_scores:
        score_numbers.append(int(player[1]))
    sorted_scores = sorted(score_numbers, reverse=True)
    score_numbers.clear()
    while highest_scores != []:
        for index, score in enumerate(highest_scores):
            if int(score[1]) == sorted_scores[0]:
                score_numbers.append(score)
                sorted_scores.remove(sorted_scores[0])
                highest_scores.remove(score)
    with open("best_highscores.csv", "w", newline='') as file2:
        writer = csv.writer(file2)
        for i in score_numbers:
            writer.writerow(i)
                    


if __name__ == "__main__":
    game_played()
    highscores()