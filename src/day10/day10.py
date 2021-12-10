from functools import reduce


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
    stack = Stack()
    with open("day10input.txt", 'r') as file:
        lines = [line for line in file]
        # get lines whose syntax check score == 0 (not corrupt)
        clean_lines = list(
            filter(lambda line: syntax_check(line, stack) == 0, lines))
        completers = list(
            map(lambda line: get_completer(line, stack), clean_lines))
        scores = list(
            map(lambda complete: get_autocomplete_score(complete), completers))
        sorted_scores = sorted(scores)
        print(sorted_scores[len(sorted_scores) // 2])


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

    def purge(self):
        remaining = ""
        while (len(self.stack) > 0):
            remaining += self.stack.pop()
        return remaining


# Part one functions
def syntax_check(line: str, stack: Stack) -> int:
    # count = 0
    for char in line:
        if char in ['<', '(', '{', '[']:
            stack.push(char)
        elif char in ['>', ')', '}', ']']:
            latest = stack.pop()
            if (not is_match(latest, char)):
                stack.reset()
                # print("Syntax error: Expected", latest,
                # "but got", char, "Column:", count)
                return get_syntax_score(char)
        # count += 1
    stack.reset()
    return 0


def is_match(bracket_one: str, bracket_two: str):
    return ((bracket_one == '[' and bracket_two == ']')
            or (bracket_one == '{' and bracket_two == '}')
            or (bracket_one == '<' and bracket_two == '>')
            or (bracket_one == '(' and bracket_two == ')'))


def get_syntax_score(bracket: str) -> int:
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


# Part two functions
def get_completer(line: str, stack: Stack) -> str:

    def return_pair(bracket: str) -> int:
        if (bracket == '('):
            return ')'
        elif (bracket == '['):
            return ']'
        elif (bracket == '{'):
            return '}'
        elif (bracket == '<'):
            return '>'
        else:
            raise ValueError("Not a closing bracket")

    for char in line:
        if char in ['<', '(', '{', '[']:
            stack.push(char)
        elif char in ['>', ')', '}', ']']:
            latest = stack.pop()
            if (not is_match(latest, char)):
                raise ValueError("Mismatch found")
    remainder = stack.purge()
    completer = map(lambda char: return_pair(char), remainder)
    return completer


def get_autocomplete_score(line: str):

    def get_bracket_value(bracket: str):
        if (bracket == ')'):
            return 1
        elif (bracket == ']'):
            return 2
        elif (bracket == '}'):
            return 3
        elif (bracket == '>'):
            return 4
        else:
            raise ValueError("Not a closing bracket")

    return reduce(lambda curr, next: curr * 5 + get_bracket_value(next), line, 0)


if __name__ == "__main__":
    main()
