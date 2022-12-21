import re


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def build_map():
    lines = read_file()
    re_num = re.compile(r"(\w+): (\d+)")
    re_op = re.compile(r"(\w+): (\w+) (\+|\-|\*|\/) (\w+)")
    mmap = {}

    for line in lines:
        res_num = re_num.search(line)
        if res_num:
            monkey, num = res_num.groups()
            mmap[monkey] = int(num)
            continue
        res_op = re_op.search(line)
        if res_op:
            monkey, m1, sign, m2 = res_op.groups()
            mmap[monkey] = (m1, sign, m2)
            continue

    return mmap


def get_op(sign):
    match sign:
        case "+":
            return lambda m1, m2: m1 + m2
        case "-":
            return lambda m1, m2: m1 - m2
        case "*":
            return lambda m1, m2: m1 * m2
        case "/":
            return lambda m1, m2: int(m1 / m2)


def get_monkey_number(monkey, mmap):
    val = mmap[monkey]

    if type(val) is int:
        return val
    if val is None:
        return None

    m1, sign, m2 = val
    m1_val = get_monkey_number(m1, mmap)
    m2_val = get_monkey_number(m2, mmap)
    if m1_val is None or m2_val is None:
        return None
    return get_op(sign)(m1_val, m2_val)


def part_1():
    mmap = build_map()
    print(get_monkey_number("root", mmap))


def build_inverse_map():
    lines = read_file()
    re_plus = re.compile(r"(\w+): (\w+) \+ (\w+)")
    re_minus = re.compile(r"(\w+): (\w+) \- (\w+)")
    re_mul = re.compile(r"(\w+): (\w+) \* (\w+)")
    re_div = re.compile(r"(\w+): (\w+) \/ (\w+)")
    immap = {}

    for line in lines:
        res_plus = re_plus.search(line)
        if res_plus:
            monkey, m1, m2 = res_plus.groups()
            immap[m1] = (monkey, "-", m2)
            immap[m2] = (monkey, "-", m1)
            continue
        res_minus = re_minus.search(line)
        if res_minus:
            monkey, m1, m2 = res_minus.groups()
            immap[m1] = (monkey, "+", m2)
            immap[m2] = (m1, "-", monkey)
            continue
        res_mul = re_mul.search(line)
        if res_mul:
            monkey, m1, m2 = res_mul.groups()
            immap[m1] = (monkey, "/", m2)
            immap[m2] = (monkey, "/", m1)
            continue
        res_div = re_div.search(line)
        if res_div:
            monkey, m1, m2 = res_div.groups()
            immap[m1] = (monkey, "*", m2)
            immap[m2] = (m1, "/", monkey)
            continue

    return immap


def is_humn_side(monkey, mmap):
    val = mmap[monkey]

    if monkey == "humn":
        return True

    if type(val) is int:
        return False

    m1, _, m2 = val
    return is_humn_side(m1, mmap) or is_humn_side(m2, mmap)


def get_monkey_number_inverse(monkey, mmapn, immap):
    # If we can find the num with the regular map, we get it
    num = get_monkey_number(monkey, mmapn)
    if num:
        return num

    # Else it's on humn path so we need to get the value from the inverse map
    val = immap[monkey]
    if type(val) is int:
        return val
    m1, sign, m2 = val

    m1_val = get_monkey_number_inverse(m1, mmapn, immap)
    m2_val = get_monkey_number_inverse(m2, mmapn, immap)
    return get_op(sign)(m1_val, m2_val)


def part_2():
    mmap = build_map()
    immap = build_inverse_map()

    mmapn = mmap.copy()
    mmapn["humn"] = None

    m1, _, m2 = mmap["root"]
    if is_humn_side(m1, mmap):
        m2_num = get_monkey_number(m2, mmapn)
        immap[m1] = m2_num
    else:
        m1_num = get_monkey_number(m1, mmapn)
        immap[m2] = m1_num

    print(get_monkey_number_inverse("humn", mmapn, immap))


part_1()
part_2()
