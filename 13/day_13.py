import json
import itertools
import functools


def read_pairs():
    with open("input.txt") as file:
        return list(
            map(lambda pair: pair.split("\n"), file.read().strip().split("\n\n"))
        )


def is_in_right_order(p1, p2):
    res = None

    # Ran out of items
    if p1 == None:
        return True
    if p2 == None:
        return False

    # Compare integers
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 == p2:
            return None
        if p1 < p2:
            return True
        if p1 > p2:
            return False

    # Convert type if necessary
    p1 = [p1] if not isinstance(p1, list) else p1
    p2 = [p2] if not isinstance(p2, list) else p2

    # Handle lists
    # zip_longest is for padding "None" for shorter lists when zipping
    ziped = list(itertools.zip_longest(p1, p2))
    while ziped:
        z1, z2 = ziped.pop(0)
        rres = is_in_right_order(z1, z2)
        if rres == None:
            continue
        else:
            res = rres
            break

    return res


def part_1():
    pairs = read_pairs()
    res = 0
    for i, (p1, p2) in enumerate(pairs):
        # Use json to deserialize strings as lists
        p1 = json.loads(p1)
        p2 = json.loads(p2)

        if is_in_right_order(p1, p2):
            res += i + 1

    print(res)


def part_2():
    packets = list(map(json.loads, itertools.chain(*read_pairs())))
    d1 = [[2]]
    d2 = [[6]]
    packets.append(d1)
    packets.append(d2)

    # We can use is_in_right_order as a comparison function for sorting all packets
    sorted_packets = sorted(
        packets,
        key=functools.cmp_to_key(lambda p1, p2: -1 if is_in_right_order(p1, p2) else 1),
    )

    print((sorted_packets.index(d1) + 1) * (sorted_packets.index(d2) + 1))


part_1()
part_2()
