def get_elves_calories():
    with open("input.txt") as file:
        chunks = file.read().split("\n\n")
        return [tuple(map(int, chunk.split())) for chunk in chunks]


def part_1():
    elves_calories = get_elves_calories()
    highest = max(map(sum, elves_calories))
    print(highest)


def part_2():
    elves_calories = get_elves_calories()
    elves_calories.sort(key=sum, reverse=True)
    highest_3 = sum(map(sum, elves_calories[:3]))
    print(highest_3)


# part_1()
# part_2()
