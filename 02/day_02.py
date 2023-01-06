def read_file():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
        return [line.split() for line in lines]


def get_shape_score(shape):
    match shape:
        case "R":
            return 1
        case "P":
            return 2
        case "S":
            return 3


def get_outcome_score(round):
    match round:
        case ["A", "R"]:
            return 3
        case ["A", "P"]:
            return 6
        case ["A", "S"]:
            return 0
        case ["B", "R"]:
            return 0
        case ["B", "P"]:
            return 3
        case ["B", "S"]:
            return 6
        case ["C", "R"]:
            return 6
        case ["C", "P"]:
            return 0
        case ["C", "S"]:
            return 3


def part_1():
    rounds = read_file()
    total_score = 0
    for round in rounds:
        match round[1]:
            case "X":
                round[1] = "R"
            case "Y":
                round[1] = "P"
            case "Z":
                round[1] = "S"
        total_score += get_shape_score(round[1]) + get_outcome_score(round)
    print(total_score)


def get_game():
    return {
        "A": {"wins": "P", "draws": "R", "loses": "S"},
        "B": {"wins": "S", "draws": "P", "loses": "R"},
        "C": {"wins": "R", "draws": "S", "loses": "P"},
    }


def part_2():
    rounds = read_file()
    game = get_game()
    total_score = 0
    for round in rounds:
        match round[1]:
            case "X":
                round[1] = game.get(round[0]).get("loses")
            case "Y":
                round[1] = game.get(round[0]).get("draws")
            case "Z":
                round[1] = game.get(round[0]).get("wins")

        total_score += get_shape_score(round[1]) + get_outcome_score(round)
    print(total_score)


part_1()
part_2()
