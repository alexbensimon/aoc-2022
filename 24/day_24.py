def read_file():
    with open("input.txt") as file:
        grid = [list(line) for line in file.read().strip().split("\n")]
        bliz = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] not in ["#", "."]:
                    bliz.append((grid[r][c], (r, c)))
        max_r = len(grid) - 2
        max_c = len(grid[0]) - 2
        return bliz, max_r, max_c


directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def verify_next(next, max):
    if next < 1:
        next = max
    elif next > max:
        next = 1
    return next


def move_bliz(bliz, max_r, max_c):
    new_bliz = []
    for dir, pos in bliz:
        r, c = pos
        i, j = directions[dir]
        next_r = verify_next(r + i, max_r)
        next_c = verify_next(c + j, max_c)
        new_bliz.append((dir, (next_r, next_c)))
    return new_bliz


def find_neighbors(curr, bliz, max_r, max_c):
    occupied = set([pos for _, pos in bliz])
    neighbors = []
    r, c = curr
    for i, j in directions.values():
        next_r = r + i
        next_c = c + j
        if (
            next_r >= 1
            and next_r <= max_r
            and next_c >= 1
            and next_c <= max_c
            and (next_r, next_c) not in occupied
        ):
            neighbors.append((next_r, next_c))

    # We can stay in the same position
    if curr not in occupied:
        neighbors.append(curr)

    # Special cases for start and end
    if curr == (1, 1):
        neighbors.append((0, 1))
    elif curr == (max_r, max_c):
        neighbors.append((max_r + 1, max_c))

    return neighbors


def find_best_time(src, dest, bliz, max_r, max_c):
    positions = set([src])
    time = 0
    while dest not in positions:
        time += 1
        bliz = move_bliz(bliz, max_r, max_c)

        new_positions = set()
        for pos in positions:
            neighbors = find_neighbors(pos, bliz, max_r, max_c)
            new_positions.update(neighbors)

        positions = new_positions

    return time, bliz


def part_1():
    bliz, max_r, max_c = read_file()
    time, _ = find_best_time((0, 1), (max_r + 1, max_c), bliz, max_r, max_c)
    print(time)


def part_2():
    bliz, max_r, max_c = read_file()
    start = (0, 1)
    end = (max_r + 1, max_c)
    time1, bliz = find_best_time(start, end, bliz, max_r, max_c)
    time2, bliz = find_best_time(end, start, bliz, max_r, max_c)
    time3, bliz = find_best_time(start, end, bliz, max_r, max_c)
    print(time1 + time2 + time3)


part_1()
part_2()
