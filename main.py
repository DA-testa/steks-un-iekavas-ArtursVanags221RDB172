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
           opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1


               
            nig = opening_brackets_stack.pop()
            if not are_matching(nig.char, next):
                return i+1
            
    if  opening_brackets_stack:
        nig = opening_brackets_stack.pop()
        return nig.position + 1

    return "Success"


def main():
    select_input = input("input - F or I")
    if select_input.upper() == "F":
        file_path = input("choose file (input path)")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == "Success":
                 print("Success")
            else:
                 print(mismatch)
    else:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()
