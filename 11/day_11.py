import math

# Quicker to copy input than parsing it
def get_test_monkeys():
    return [
        {
            "items": [79, 98],
            "op": lambda old: old * 19,
            "test": (23, 2, 3),
        },
        {
            "items": [54, 65, 75, 74],
            "op": lambda old: old + 6,
            "test": (19, 2, 0),
        },
        {
            "items": [79, 60, 97],
            "op": lambda old: old * old,
            "test": (13, 1, 3),
        },
        {
            "items": [74],
            "op": lambda old: old + 3,
            "test": (17, 0, 1),
        },
    ]


def get_input_monkeys():
    return [
        {
            "items": [92, 73, 86, 83, 65, 51, 55, 93],
            "op": lambda old: old * 5,
            "test": (11, 3, 4),
        },
        {
            "items": [99, 67, 62, 61, 59, 98],
            "op": lambda old: old * old,
            "test": (2, 6, 7),
        },
        {
            "items": [81, 89, 56, 61, 99],
            "op": lambda old: old * 7,
            "test": (5, 1, 5),
        },
        {
            "items": [97, 74, 68],
            "op": lambda old: old + 1,
            "test": (17, 2, 5),
        },
        {
            "items": [78, 73],
            "op": lambda old: old + 3,
            "test": (19, 2, 3),
        },
        {
            "items": [50],
            "op": lambda old: old + 5,
            "test": (7, 1, 6),
        },
        {
            "items": [95, 88, 53, 75],
            "op": lambda old: old + 8,
            "test": (3, 0, 7),
        },
        {
            "items": [50, 77, 98, 85, 94, 56, 89],
            "op": lambda old: old + 2,
            "test": (13, 4, 0),
        },
    ]


def part_1():
    monkeys = get_input_monkeys()
    inspects = [0] * len(monkeys)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                inspects[i] += 1
                item = math.floor(monkey["op"](item) / 3)
                divisor, option1, option2 = monkey["test"]
                receiver = option1 if item % divisor == 0 else option2
                monkeys[receiver]["items"].append(item)
            monkeys[i]["items"] = []
    inspects.sort(reverse=True)
    first, second, *_ = inspects
    print(first * second)


def part_2():
    monkeys = get_input_monkeys()
    inspects = [0] * len(monkeys)
    # We need the least common multiple of all the monkeys divisors
    # This value is the "cycle" that each item can go through without changing the divisibility tests
    modulus = math.lcm(*map(lambda monkey: monkey["test"][0], monkeys))
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                inspects[i] += 1
                item = monkey["op"](item)
                divisor, option1, option2 = monkey["test"]
                receiver = option1 if item % divisor == 0 else option2
                # We can preserve the divisability of the items and keep their value small enough to do the computation
                monkeys[receiver]["items"].append(item % modulus)
            monkeys[i]["items"] = []
    inspects.sort(reverse=True)
    first, second, *_ = inspects
    print(first * second)


part_1()
part_2()
