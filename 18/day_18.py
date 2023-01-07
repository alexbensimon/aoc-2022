from operator import itemgetter
from collections import deque


def read_file():
    with open("input.txt") as file:
        return [
            tuple(map(int, line.split(","))) for line in file.read().strip().split("\n")
        ]


def surface_area(cubes):
    cubes_sides_exposed = []

    for cube in cubes:
        sides_exposed = 6

        for other in cubes:
            if other == cube:
                continue

            x, y, z = cube
            ox, oy, oz = other

            if (
                ((x, y) == (ox, oy) and abs(z - oz) == 1)
                or ((y, z) == (oy, oz) and abs(x - ox) == 1)
                or ((x, z) == (ox, oz) and abs(y - oy) == 1)
            ):
                sides_exposed -= 1
        cubes_sides_exposed.append(sides_exposed)
    return sum(cubes_sides_exposed)


def part_1():
    cubes = read_file()
    print(surface_area(cubes))


def neighbors(cube):
    x, y, z = cube
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


def find_trapped_sides(cube, cubes, range_x, range_y, range_z):
    visited = set()
    queue = deque([cube])
    trapped_sides = 0

    while queue:
        current = queue.pop()
        if current in visited:
            continue
        visited.add(current)

        x, y, z = current
        if x not in range_x or y not in range_y or z not in range_z:
            return 0, visited

        # Test all neighbors until we go out of range or positions to visit
        for neighbor in neighbors(current):
            if neighbor in cubes:
                trapped_sides += 1
            elif neighbor not in visited:
                queue.append(neighbor)

    return trapped_sides, visited


def part_2():
    cubes = read_file()

    exterior_surface_area = surface_area(cubes)

    max_x, _, _ = max(cubes, key=itemgetter(0))
    min_x, _, _ = min(cubes, key=itemgetter(0))
    range_x = range(min_x, max_x + 1)
    _, max_y, _ = max(cubes, key=itemgetter(1))
    _, min_y, _ = min(cubes, key=itemgetter(1))
    range_y = range(min_y, max_y + 1)
    _, _, max_z = max(cubes, key=itemgetter(2))
    _, _, min_z = min(cubes, key=itemgetter(2))
    range_z = range(min_z, max_z + 1)

    visited = set()
    for x in range_x:
        for y in range_y:
            for z in range_z:
                if (x, y, z) not in cubes and (x, y, z) not in visited:
                    # Test if is surrounded
                    trapped_sides, c_visited = find_trapped_sides(
                        (x, y, z), cubes, range_x, range_y, range_z
                    )
                    exterior_surface_area -= trapped_sides
                    visited |= c_visited

    print(exterior_surface_area)


part_1()
part_2()
