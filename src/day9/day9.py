def main():
    partOne()
    partTwo()


def partOne():
    with open("day9input.txt", 'r') as file:
        matrix = parse_into_matrix(file)
        height = len(matrix)
        width = len(matrix[0])
        count = 0
        for i in range(height):
            for j in range(width):
                if (is_valley(matrix, i, j)):
                    count += (matrix[i][j] + 1)
        print(count)


def partTwo():
    return 0


def parse_into_matrix(numbers: list) -> list:
    matrix = []
    for line in numbers:
        row = []
        for number in line:
            if number != '\n':
                row.append(int(number))
        matrix.append(row)
    return matrix


def is_valley(matrix: list, row: int, column: int) -> bool:
    value = matrix[row][column]

    top = get_top(matrix, row, column)
    bottom = get_bottom(matrix, row, column)
    left = get_left(matrix, row, column)
    right = get_right(matrix, row, column)

    neighbours = [top, bottom, left, right]
    answer = all([value < x for x in neighbours])
    return answer


def get_top(matrix: list, row: int, column: int) -> int:
    if (row == 0):
        return 10
    else:
        return matrix[row - 1][column]


def get_bottom(matrix: list, row: int, column: int) -> int:
    height = len(matrix)
    if (row == height - 1):
        return 10
    else:
        return matrix[row + 1][column]


def get_left(matrix: list, row: int, column: int) -> int:
    if (column == 0):
        return 10
    else:
        return matrix[row][column - 1]


def get_right(matrix: list, row: int, column: int) -> int:
    width = len(matrix[0])
    if (column == width - 1):
        return 10
    else:
        return matrix[row][column + 1]


if __name__ == "__main__":
    main()
