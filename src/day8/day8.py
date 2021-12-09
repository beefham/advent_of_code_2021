def main():
    partOne()
    partTwo()


def partOne():
    with open("day8input.txt", "r") as file:
        second_half = [line.split(' | ')[1] for line in file]
        count = 0
        for line in second_half:
            digits = line.split()
            for segments in digits:
                if (len(segments) in (2, 3, 4, 7)):
                    count += 1
        print(count)


# For part 2: maps a letter to a value for identification
prime_map = {'a': 2,
             'b': 3,
             'c': 5,
             'd': 7,
             'e': 11,
             'f': 13,
             'g': 17}


def partTwo():
    """
    Start by sorting out each string that represents the digits.

    We can identify any of the four digits 1, 4, 7, 8 by length.

    Digits 0, 6, 9 can be found by finding those with length 6.
        Digit 0
        Digit 6

    Digits 2, 3, 5 are those with length 5.
        Digit 3 is the only one that shares letters with 1.

    After identifying 1,4,7,8, we can identify 3
    After identifying 3, we can find common parts between 2 and 5 to find the 3 horizontal segments
    With the 3 horizontal segments, we can identify 0 as the one that does not contain any of the horizontal segments

    Example:
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe

    Length 5: cdefg / abcdf / bcdef (2,3,5)
    Length 6: bcdefg / acdefg / abdefg (0,6,9)

    From the front part:
    1: be
    4: bceg
    7: bde
    8: abcdefg // 8 is always this

    2: (cdefg) / abcdf / bcdef -> is a subset of digit 6 from below
    3: cdefg / abcdf / (bcdef) -> because it contains both 'b' and 'e'
    5: cdefg / (abcdf) / bcdef -> by elimination

    From 'cdefg' and 'abcdf', it is clear 'cdf' map to the 3 horizontal segments
    Then, we can tell 'b' and 'e' are one pair of vertical lines (the right pair (obvious when we see the digit 1))
        and 'a', 'g' make up the left pair.

    Since 4 contains 'g' but not 'a', we know that the top left segment is wired to 'g'

    From the digit 1, we can identify 6, as 6 is the only digit that does not contain 1 in 7-segment display.

    6: bcdefg / (acdefg) / abdefg -> does not have both 'b' and 'e'
    9: (bcdefg) / acdefg / abdefg -> by elimination
    0: bcdefg / acdefg / (abdefg) -> because it is missing 'c'

    Therefore, we can find (1,4,7,8), then use them to find (6, 3), then use them to find (2, 0), then finally find (5, 9)
    """
    with open("day8input.txt", 'r') as file:
        answer = 0
        print(answer)


def parse_line(line: str):
    halves = line.split(' | ')
    clues = halves[0]
    digits = halves[1]
    segment_map = {}
    for clue in clues.split():
        clue = "".join(sorted(clue))
        if (len(clue) == 2):
            segment_map[clue] = 1
        if (len(clue) == 3):
            segment_map[clue] = 7
        if (len(clue) == 4):
            segment_map[clue] = 4
        if (len(clue) == 7):
            segment_map[clue] = 8


def break_into_char(clue: str):
    char_set = set()
    for char in clue:
        char_set.add(char)
    return char_set


if __name__ == "__main__":
    main()
