import re
import functools


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_report():
    lines = read_file()
    regex = re.compile(
        r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    )
    rate = {}
    connexions = {}
    for line in lines:
        valve, r, tunnels = regex.search(line).groups()
        rate[valve] = int(r)
        connexions[valve] = tunnels.split(", ")
    return rate, connexions


def part_1():
    rate, connexions = parse_report()

    # Cache so that we only compute a given configuration once
    @functools.cache
    def max_release(current, opens, min_left):
        # No need to go further because we won't have time to release more pressure
        if min_left <= 1:
            return 0

        # We compute the results for each neighbor and keep the highest
        max_r = max(max_release(v, opens, min_left - 1) for v in connexions[current])

        # If it makes sense to open to current valve, we also try it
        if rate[current] > 0 and current not in opens:
            # Result is the release we get for all minutes after this valve is open + the result from the next position
            max_r = max(
                max_r,
                rate[current] * (min_left - 1)
                + max_release(current, frozenset((*opens, current)), min_left - 1),
            )

        return max_r

    # frozenset is an immutable set and helps to optimize the cache
    print(max_release("AA", frozenset(), 30))


def part_2():
    rate, connexions = parse_report()

    @functools.cache
    def max_release(current, opens, min_left, has_elephant):
        if min_left <= 1:
            # If we're done for this path, we compute again for the elephant
            return max_release("AA", opens, 26, False) if has_elephant else 0

        max_r = max(
            max_release(v, opens, min_left - 1, has_elephant)
            for v in connexions[current]
        )

        if rate[current] > 0 and current not in opens:
            max_r = max(
                max_r,
                rate[current] * (min_left - 1)
                + max_release(
                    current, frozenset((*opens, current)), min_left - 1, has_elephant
                ),
            )

        return max_r

    print(max_release("AA", frozenset(), 26, True))


part_1()
part_2()
