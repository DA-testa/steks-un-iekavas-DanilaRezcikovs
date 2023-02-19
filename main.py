# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


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


def main():
    input_type = input().strip()
    if input_type.isdigit() and int(input_type) in range(6):
        test_number = input_type
        test_path = "/workspaces/steks-un-iekavas-DanilaRezcikovs/test/" + test_number
        with open (test_path, "r") as f:
            text = f.read().strip()
    elif input_type == "I":
        text = input("Enter brackets: ")
    else:
        print("Invalid input type")
        return

    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
