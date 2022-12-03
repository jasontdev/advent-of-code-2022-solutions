import fileinput

# Part 1
shape_score = {'X': 1, 'Y': 2, 'Z': 3}
response = {'A': ['Z', 'X', 'Y'], 'B': ['X', 'Y', 'Z'], 'C': ['Y', 'Z', 'X']}


def total_score(input_file):
    results = []

    for line in fileinput.input(input_file):
        opponents_move, your_move = line.rstrip('\n').split(" ")
        result = response.get(opponents_move).index(your_move)
        results.append(shape_score.get(your_move) + result * 3)

    return sum(results)


print(total_score("input"))


# Part 2
result_score = {'X': 0, 'Y': 1, 'Z': 2}  # loss, draw, win


def total_score2(input_file):
    results = []

    for line in fileinput.input(input_file):
        opponents_move, outcome = line.rstrip('\n').split(" ")

        # find the response to opponent's move that will achieve the outcome:
        your_move = response.get(opponents_move)[result_score.get(outcome)]
        score = shape_score[your_move] + (result_score[outcome] * 3)
        results.append(score)

    return sum(results)


print(total_score2("input"))

