players = ["player_1", "player_2", "player_3"]
list_of_lists = [["player_1", 10], ["player_1", 10], ["player_3", 10], ["player_3", 9], ["player_2", 9], ["player_2", 7], ["player_3", 6]]
list_of_lists_2 = []
while players != []:
    for result in list_of_lists:
        if result[0] in players:
            list_of_lists_2.append(result)
            players.remove(result[0])
print(list_of_lists_2)