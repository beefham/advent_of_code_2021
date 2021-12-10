def main():
    partOne()
    partTwo()


def partOne():
    stack = Stack()
    with open("day10input.txt", 'r') as file:
        total = 0
        for line in file:
            score = syntax_check(line, stack)
            total += score
        print(total)


def partTwo():
    return 0


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        value = self.stack.pop()
        return value

    def reset(self):
        self.stack = []


def syntax_check(line: str, stack: Stack) -> int:
    count = 0
    for char in line:
        if char in ['<', '(', '{', '[']:
            stack.push(char)
        elif char in ['>', ')', '}', ']']:
            latest = stack.pop()
            if (not is_match(latest, char)):
                stack.reset()
                print("Syntax error: Expected", latest,
                      "but got", char, "Column:", count)
                return get_score(char)
        count += 1
    stack.reset()
    return 0


def is_match(bracket_one: str, bracket_two: str):
    return ((bracket_one == '[' and bracket_two == ']')
            or (bracket_one == '{' and bracket_two == '}')
            or (bracket_one == '<' and bracket_two == '>')
            or (bracket_one == '(' and bracket_two == ')'))


def get_score(bracket: str) -> int:
    if (bracket == ')'):
        return 3
    elif (bracket == ']'):
        return 57
    elif (bracket == '}'):
        return 1197
    elif (bracket == '>'):
        return 25137
    else:
        raise ValueError("Not a closing bracket")


if __name__ == "__main__":
    main()
