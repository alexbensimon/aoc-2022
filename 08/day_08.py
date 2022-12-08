def read_file():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
        return list(map(list, lines))


def part_1():
    grid = read_file()
    visible_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # left
            is_visible = True
            i = col - 1
            while i >= 0:
                if grid[row][i] >= grid[row][col]:
                    is_visible = False
                    # We can stop looking as soon as a tree is bigger
                    break
                i -= 1
            if is_visible:
                visible_count += 1
                # If a tree is visible in one direction, we don't need to check other directions
                continue

            # right
            is_visible = True
            i = col + 1
            while i < len(grid[row]):
                if grid[row][i] >= grid[row][col]:
                    is_visible = False
                    break
                i += 1
            if is_visible:
                visible_count += 1
                continue

            # top
            is_visible = True
            i = row - 1
            while i >= 0:
                if grid[i][col] >= grid[row][col]:
                    is_visible = False
                    break
                i -= 1
            if is_visible:
                visible_count += 1
                continue

            # bottom
            is_visible = True
            i = row + 1
            while i < len(grid):
                if grid[i][col] >= grid[row][col]:
                    is_visible = False
                    break
                i += 1
            if is_visible:
                visible_count += 1
                continue

    print(visible_count)


def part_2():
    grid = read_file()
    highest_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree_score = 1

            # left
            dir_score = 0
            i = col - 1
            while i >= 0:
                dir_score += 1
                if grid[row][i] >= grid[row][col]:
                    break
                i -= 1
            if dir_score == 0:
                # If a score in one direction is 0, we don't need to check other directions
                continue
            else:
                tree_score *= dir_score

            # right
            dir_score = 0
            i = col + 1
            while i < len(grid[row]):
                dir_score += 1
                if grid[row][i] >= grid[row][col]:
                    break
                i += 1
            if dir_score == 0:
                continue
            else:
                tree_score *= dir_score

            # top
            dir_score = 0
            i = row - 1
            while i >= 0:
                dir_score += 1
                if grid[i][col] >= grid[row][col]:
                    break
                i -= 1
            if dir_score == 0:
                continue
            else:
                tree_score *= dir_score

            # bottom
            dir_score = 0
            i = row + 1
            while i < len(grid):
                dir_score += 1
                if grid[i][col] >= grid[row][col]:
                    break
                i += 1
            if dir_score == 0:
                continue
            else:
                tree_score *= dir_score

            highest_score = max(tree_score, highest_score)

    print(highest_score)


part_1()
part_2()
