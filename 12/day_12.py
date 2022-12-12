def read_file():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
        return list(map(list, lines))


def elevation_cost(item):
    if item == "S":
        return ord("a")
    if item == "E":
        return ord("z")
    return ord(item)


def can_go(origin, dest):
    return elevation_cost(dest) - elevation_cost(origin) <= 1


def can_go_reverse(origin, dest):
    return elevation_cost(dest) - elevation_cost(origin) >= -1


def find_possible_moves(row, col, grid, can_go_fn):
    current = grid[row][col]
    possible_moves = []
    if row + 1 < len(grid) and can_go_fn(current, grid[row + 1][col]):
        possible_moves.append((row + 1, col))
    if row - 1 >= 0 and can_go_fn(current, grid[row - 1][col]):
        possible_moves.append((row - 1, col))
    if col + 1 < len(grid[row]) and can_go_fn(current, grid[row][col + 1]):
        possible_moves.append((row, col + 1))
    if col - 1 >= 0 and can_go_fn(current, grid[row][col - 1]):
        possible_moves.append((row, col - 1))
    return possible_moves


# Breadth-first search
def find_lowest_steps(starting_position, grid, can_go_fn, dest_item):
    queue = [(0, starting_position)]
    visited = set()

    while queue:
        steps, position = queue.pop(0)
        row, col = position
        if grid[row][col] == dest_item:
            return steps

        if position not in visited:
            visited.add(position)
            for move in find_possible_moves(row, col, grid, can_go_fn):
                if move not in visited:
                    queue.append((steps + 1, move))


def find_item_position(item, grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == item:
                return (r, c)


def part_1():
    grid = read_file()
    starting_position = find_item_position("S", grid)
    res = find_lowest_steps(starting_position, grid, can_go, "E")
    print(res)


def part_2():
    grid = read_file()

    # We can start at the end position and stop when we find the first "a"
    starting_position = find_item_position("E", grid)
    res = find_lowest_steps(starting_position, grid, can_go_reverse, "a")
    print(res)


part_1()
part_2()
