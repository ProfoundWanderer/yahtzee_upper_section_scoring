def yahtzee_upper(roll_list):
    possible_scores = []
    for roll in roll_list:
        possible_scores.append(roll_list.count(roll) * roll)

    return max(possible_scores)


print(yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864]))
