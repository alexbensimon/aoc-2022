import re


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_line(line, regex):
    xs, ys, xb, yb = map(int, regex.search(line).groups())
    return ((xs, ys), (xb, yb))


def parse_report():
    lines = read_file()
    regex = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    return list(map(lambda line: parse_line(line, regex), lines))


def man_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def precompute_sbdists(sbs):
    return [(sensor, beacon, man_dist(sensor, beacon)) for (sensor, beacon) in sbs]


def find_min_max_x(sbds):
    max_sb_dist = max([dist for (_, _, dist) in sbds])
    sx_list = [xs for ((xs, _), _, _) in sbds]
    min_x = min(sx_list) - max_sb_dist
    max_x = max(sx_list) + max_sb_dist
    return min_x, max_x


def part_1():
    sbs = parse_report()
    sbds = precompute_sbdists(sbs)
    min_x, max_x = find_min_max_x(sbds)
    y = 2000000
    no_beacon_xs = set()
    for x in range(min_x, max_x):
        for (sensor, _, sb_dist) in sbds:
            sx_dist = man_dist(sensor, (x, y))
            if sx_dist <= sb_dist:
                no_beacon_xs.add(x)
                break

    # Remove known beacon positions
    beacons = [b for (_, b) in sbs]
    no_beacon_xs = list(filter(lambda x: (x, y) not in beacons, no_beacon_xs))
    print(len(no_beacon_xs))


def check_position(position, sbds, max):
    x, y = position
    if x > max or y > max:
        return False
    for (sensor, _, sb_dist) in sbds:
        sp_dist = man_dist(sensor, position)
        if sp_dist <= sb_dist:
            return False
    return True


def part_2():
    sbs = parse_report()
    sbds = precompute_sbdists(sbs)
    max = 4000000
    beacon = None
    x, y = (0, 0)
    while x < max or y < max:
        print(x, y)
        if x > max:
            x = 0
            y += 1
        for (sensor, _, sb_dist) in sbds:
            sp_dist = man_dist(sensor, (x, y))
            xs, ys = sensor
            if sp_dist <= sb_dist:
                x = xs + sb_dist - abs(y - ys) + 1
                break
        else:
            beacon = (x, y)
            break

    print(beacon)
    x, y = beacon
    print(x * 4000000 + y)


# part_1()
part_2()
