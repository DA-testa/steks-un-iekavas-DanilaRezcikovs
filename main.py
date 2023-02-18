from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

# changed the are_matching function to check individual bracket closures
def are_matching(left, right):
    return left == "(" and right == ")" or left == "[" and right == "]" or left == "{" and right == "}"

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))

        if next_char in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i + 1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position + 1

    return "Success"


def main
