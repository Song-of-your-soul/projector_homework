def pick_cat(cats: int, pick: int) -> list:
    round = pick
    picked_cats = []
    for number in range(cats + 1)[1:]:
        if number == round:
            picked_cats.append(number)
            round += pick
    return picked_cats


def cats_in_hats(cats: int, rounds: int) -> list:
    round = 1
    cats_with_hats = []
    while round <= rounds:
        checked_cats = pick_cat(cats, round)
        for cat in checked_cats:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)
        round += 1
    return cats_with_hats


print(cats_in_hats(100, 100))
