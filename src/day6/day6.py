def main():
    partOne()
    partTwo()


def parse_string(input: str) -> list:
    string_list = input.split(",")
    int_list = [int(i) for i in string_list]
    return int_list


def count_lanternfish(fish_list: list) -> list:
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in fish_list:
        count_list[i] += 1
    return count_list


def simulate_one_day(counted_fish: list) -> list:
    # number of 0s becomes number of 8s and 6s
    # number of Xs becomes number of (X - 1)s when X != 0
    timer_zero = counted_fish[0]
    for i in range(len(counted_fish) - 1):
        counted_fish[i] = counted_fish[i + 1]
    counted_fish[6] += timer_zero
    counted_fish[8] = timer_zero

    return counted_fish


def simulate_one_day_immutable(counted_fish: list) -> list:
    timer_zero = counted_fish[0]
    next_counted_fish = []
    for i in range(len(counted_fish)):
        next_counted_fish[i] = counted_fish[i + 1]
    next_counted_fish[6] += timer_zero
    next_counted_fish[8] = timer_zero

    return next_counted_fish


def simulate_multiple_days(counted_fish: list, days: int) -> list:
    fish_timer_list = counted_fish
    for i in range(days):
        fish_timer_list = simulate_one_day(fish_timer_list)
    return fish_timer_list


def partOne():
    with open("day6input.txt", "r") as file:
        int_list = parse_string(file.readline())
        count_list = count_lanternfish(int_list)
        answer = sum(simulate_multiple_days(count_list, 80))
        print("Part one:", answer)


def partTwo():
    with open("day6input.txt", "r") as file:
        int_list = parse_string(file.readline())
        count_list = count_lanternfish(int_list)
        answer = sum(simulate_multiple_days(count_list, 256))
        print("Part two:", answer)


if __name__ == "__main__":
    main()
