import re


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_input():
    lines = read_file()
    regex = re.compile(
        r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    )
    blueprints = []
    for line in lines:
        blueprints.append(tuple(map(int, regex.search(line).groups())))

    return blueprints


# Details: https://github.com/mebeim/aoc/tree/master/2022#day-19---not-enough-minerals
def best_case_scenario(initial_amount, robots, t):
    return initial_amount + robots * (t + 1) + t * (t + 1) // 2


def max_geodes(blueprint, time):
    (
        ore_rob_cost_ore,
        clay_rob_cost_ore,
        obs_rob_cost_ore,
        obs_rob_cost_clay,
        geo_rob_cost_ore,
        geo_rob_cost_obs,
    ) = blueprint

    ORE, CLAY, OBS, GEO = range(4)

    # Since all robots mine every minute and we cannot build more than one robot per minute, we don't need more robot for each ressource than the highest price of other robots in this ressource
    max_ore_needed = max(
        ore_rob_cost_ore, clay_rob_cost_ore, obs_rob_cost_ore, geo_rob_cost_ore
    )
    max_clay_needed = obs_rob_cost_clay
    max_obs_needed = geo_rob_cost_obs

    # The queue contains each possible state
    queue = [(time, 0, 0, 0, 0, 1, 0, 0, 0, [])]
    visited = set()
    best = 0

    while queue:
        (
            time,
            ore,
            clay,
            obs,
            geo,
            ore_rob,
            clay_rob,
            obs_rob,
            geo_rob,
            could_build,
        ) = state = queue.pop()

        if state[:-1] in visited:
            continue
        visited.add(state[:-1])

        # New ressources mined
        new_ore = ore + ore_rob
        new_clay = clay + clay_rob
        new_obs = obs + obs_rob
        new_geo = geo + geo_rob
        time -= 1

        if time == 0:
            best = max(best, new_geo)
            continue

        if best_case_scenario(new_ore, ore_rob, time) < geo_rob_cost_ore:
            best = max(best, new_geo + geo_rob * time)
            continue
        if best_case_scenario(new_obs, obs_rob, time) < geo_rob_cost_obs:
            best = max(best, new_geo + geo_rob * time)
            continue
        if best_case_scenario(new_geo, geo_rob, time) < best:
            continue

        can_build = []

        # Build ore robot
        if (
            ore_rob < max_ore_needed
            and ore >= ore_rob_cost_ore
            and ORE not in could_build
        ):
            can_build.append(ORE)
            queue.append(
                (
                    time,
                    new_ore - ore_rob_cost_ore,
                    new_clay,
                    new_obs,
                    new_geo,
                    ore_rob + 1,
                    clay_rob,
                    obs_rob,
                    geo_rob,
                    [],
                )
            )
        # Build clay robot
        if (
            clay_rob < max_clay_needed
            and ore >= clay_rob_cost_ore
            and CLAY not in could_build
        ):
            can_build.append(CLAY)
            queue.append(
                (
                    time,
                    new_ore - clay_rob_cost_ore,
                    new_clay,
                    new_obs,
                    new_geo,
                    ore_rob,
                    clay_rob + 1,
                    obs_rob,
                    geo_rob,
                    [],
                )
            )
        # Build obsidian robot
        if (
            obs_rob < max_obs_needed
            and ore >= obs_rob_cost_ore
            and clay >= obs_rob_cost_clay
            and OBS not in could_build
        ):
            can_build.append(OBS)
            queue.append(
                (
                    time,
                    new_ore - obs_rob_cost_ore,
                    new_clay - obs_rob_cost_clay,
                    new_obs,
                    new_geo,
                    ore_rob,
                    clay_rob,
                    obs_rob + 1,
                    geo_rob,
                    [],
                )
            )
        # Build geode robot
        if (
            ore >= geo_rob_cost_ore
            and obs >= geo_rob_cost_obs
            and GEO not in could_build
        ):
            can_build.append(GEO)
            queue.append(
                (
                    time,
                    new_ore - geo_rob_cost_ore,
                    new_clay,
                    new_obs - geo_rob_cost_obs,
                    new_geo,
                    ore_rob,
                    clay_rob,
                    obs_rob,
                    geo_rob + 1,
                    [],
                )
            )
        # Build no robot
        if (
            ore < max_ore_needed
            or (clay_rob and clay < max_clay_needed)
            or (obs_rob and obs < max_obs_needed)
        ):
            queue.append(
                (
                    time,
                    new_ore,
                    new_clay,
                    new_obs,
                    new_geo,
                    ore_rob,
                    clay_rob,
                    obs_rob,
                    geo_rob,
                    can_build,
                )
            )

    return best


def part_1():
    blueprints = parse_input()

    res = 0
    for i, blueprint in enumerate(blueprints):
        res += (i + 1) * max_geodes(blueprint, 24)

    print(res)


def part_2():
    blueprints = parse_input()

    res = 1
    for blueprint in blueprints[:3]:
        res *= max_geodes(blueprint, 32)

    print(res)


part_1()
part_2()
