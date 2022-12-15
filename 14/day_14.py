def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def fill_rock_map(paths):
    rock_map = {}
    for path in paths:
        coords = [tuple(map(int, path.split(","))) for path in path.split(" -> ")]
        while len(coords) > 1:
            ox, oy = coords.pop(0)
            dx, dy = coords[0]
            if ox == dx:
                r = (oy, dy + 1) if oy < dy else (dy, oy + 1)
                for y in range(*r):
                    rock_map[(ox, y)] = "#"
            if oy == dy:
                r = (ox, dx + 1) if ox < dx else (dx, ox + 1)
                for x in range(*r):
                    rock_map[(x, oy)] = "#"

    return rock_map


def fall_sand(c_sand, rock_map, bottom):
    x, y = c_sand

    # Reach bottom
    if y + 1 == bottom:
        return c_sand

    # Test possible next positions:
    # Bottom
    if rock_map.get((x, y + 1)) == None:
        return fall_sand((x, y + 1), rock_map, bottom)
    # Bottom left
    elif rock_map.get((x - 1, y + 1)) == None:
        return fall_sand((x - 1, y + 1), rock_map, bottom)
    # Bottom right
    elif rock_map.get((x + 1, y + 1)) == None:
        return fall_sand((x + 1, y + 1), rock_map, bottom)
    else:
        return c_sand


def part_1():
    paths = read_file()
    rock_map = fill_rock_map(paths)
    lowest_rock = max(map(lambda coords: coords[1], rock_map.keys()))
    bottom = lowest_rock + 1

    units = 0

    while True:
        c_sand = fall_sand((500, 0), rock_map, bottom)
        if c_sand[1] == lowest_rock:
            break
        rock_map[c_sand] = "o"
        units += 1

    print(units)


def part_2():
    paths = read_file()
    rock_map = fill_rock_map(paths)
    lowest_rock = max(map(lambda coords: coords[1], rock_map.keys()))
    bottom = lowest_rock + 2

    units = 0

    while True:
        c_sand = fall_sand((500, 0), rock_map, bottom)
        rock_map[c_sand] = "o"
        units += 1
        if c_sand == (500, 0):
            break

    print(units)


part_1()
part_2()
