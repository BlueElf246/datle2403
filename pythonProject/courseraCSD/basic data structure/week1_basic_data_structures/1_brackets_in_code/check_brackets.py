# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            last=opening_brackets_stack.pop()
            if next==')' and last=='(':
                pass
            elif next==']' and last=='[':
                pass
            elif next=='}' and last=='{':
                pass
            else:
                return i
    return 'success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
