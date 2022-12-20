def read_file():
    with open("input.txt") as file:
        return [int(num) for num in file.read().strip().split("\n")]


def part_1():
    numis = list(enumerate(read_file()))

    for numi in numis.copy():
        _, num = numi
        i = numis.index(numi)
        new_i = i + num
        numis.remove(numi)
        numis.insert(len(numis) if new_i == 0 else new_i % len(numis), num)

    zero = numis.index(0)
    x = numis[(zero + 1000) % len(numis)]
    y = numis[(zero + 2000) % len(numis)]
    z = numis[(zero + 3000) % len(numis)]

    print(x + y + z)


def part_2():
    nums = read_file()
    zero_i = nums.index(0)
    key = 811589153
    numis = [(i, num * key) for i, num in enumerate(nums)]
    c_numis = numis.copy()

    for _ in range(10):
        for numi in c_numis:
            _, num = numi
            i = numis.index(numi)
            new_i = i + num
            numis.remove(numi)
            numis.insert(len(numis) if new_i == 0 else new_i % len(numis), numi)

    new_zero_i = numis.index((zero_i, 0))
    x = numis[(new_zero_i + 1000) % len(numis)][1]
    y = numis[(new_zero_i + 2000) % len(numis)][1]
    z = numis[(new_zero_i + 3000) % len(numis)][1]

    print(x + y + z)


# part_1()
part_2()
