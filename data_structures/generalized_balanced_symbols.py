"""
Created on: 22-Mar-2018
Created by: Maneesh D
"""
from __future__ import absolute_import
from Stack import Stack


def is_balanced(expression: str) -> bool:
    """Checks if a given expression is balanced or not"""
    exp_stack = Stack(100)
    index = 0
    balanced = True
    while index < len(expression):
        symbol = expression[index]
        if symbol in "([{":
            if exp_stack.push(symbol) is not False:
                print(symbol, "pushed into stack...")
        elif symbol in ")]}":
            popped_symbol = exp_stack.pop()
            if popped_symbol is not False:
                print(popped_symbol, "popped...")
                if not matches(popped_symbol, symbol):
                    balanced = False
        index += 1
    print("Expression Symbol Stack:")
    print(exp_stack)
    if exp_stack.is_empty() and balanced:
        return True
    return False


def matches(open_symbol: str, close_symbol: str) -> bool:
    """Checks if the opening and closing sybols match"""
    symbol_close_map = {"(": ")", "[": "]", "{": "}"}
    return close_symbol == symbol_close_map.get(open_symbol)


if __name__ == "__main__":
    title = "Generalized Balanced Symbols Checker"
    print()
    print(title)
    print("=" * len(title))
    # print("Expression:", "{{([2][1])}(1+3)}", "<====>", "Balanced:", is_balanced("{{([2][1])}(1+3)}"))
    # print()
    # print("Expression:", "[{()]", "<====>", "Balanced:", is_balanced("[{()]"))
    # print()
    # print("Expression:", "(3*(1+3))+((5*7)+(9/2))", "<====>", "Balanced:", is_balanced("(3*(1+3))+((5*7)+(9/2))"))
    exp_string = input("Enter the expression with parentheses: ").rstrip()
    if is_balanced(exp_string):
        print("\nEXPRESSION IS BALANCED.\n")
    else:
        print("\nEXPRESSION IS NOT BALANCED.\n")
