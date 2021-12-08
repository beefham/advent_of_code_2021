def main():
    partOne()
    partTwo()


def partOne():
    """
    Key insight for part 1:
    For any 2 integers (a, b), any integer x, where a < x < b, is a solution.
    Total fuel = (x - a) + (b - x) = (b - a) which does not depend on x.

    Idea:
    Sort the list and pair them up (smallest and greatest together, and so on).
    Effectively, this finds the most restrictive range where the answer must lie in between

    This simply becomes a matter of finding the median of the list       
    """
    with open("day7input.txt", 'r') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        crabs.sort()
        middle = (crabs[((len(crabs) - 1) // 2)] + crabs[len(crabs) // 2]) // 2
        answer = sum(list(map(lambda x: abs(x - middle), crabs)))
        print(answer)


def partTwo():
    """
    For a distance n that the crab sub has to travel, ((n + 1)(n))/2 fuel is consumed.
    Let c(n) be the cost of fuel to travel distance n, so c(n) = ((n + 1)(n)) / 2.
    To minimise the total cost, we should minimise the total distance needed to travel for all crabs.
    This essentially reduces the problem to finding the mean.
    """
    with open("day7input.txt", 'r') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        mean = (sum(crabs) / len(crabs))
        distOne = round(mean)
        distTwo = 0
        # find the two integers adjacent to mean
        if (mean > distOne):  # mean was rounded down
            distTwo = distOne + 1
        else:  # mean was rounded up
            distTwo = distOne - 1

        def getCost(distance: int) -> int:
            return (distance) * (distance + 1) // 2

        answerOne = sum(list(map(lambda x: getCost(abs(x - distOne)), crabs)))
        answerTwo = sum(list(map(lambda x: getCost(abs(x - distTwo)), crabs)))

        print(answerOne if answerOne < answerTwo else answerTwo)


if __name__ == "__main__":
    main()
