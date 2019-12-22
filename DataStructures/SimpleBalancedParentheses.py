"""
Created on: 22-Mar-2018
Created by: Maneesh D
"""
from __future__ import absolute_import
from Stack import Stack


def is_balanced(expression: str) -> bool:
    """Checks if the given expression is balanced or not"""
    exp_stack = Stack(100)
    index = 0
    while index < len(expression):
        symbol = expression[index]
        if symbol == "(":
            if exp_stack.push(symbol) is not False:
                print("( pushed into stack")
        elif symbol == ")":
            if exp_stack.pop() is not False:
                print(") popped...")
        index += 1
    print("Expression Symbol Stack:")
    print(exp_stack)
    if exp_stack.is_empty():
        return True
    return False


if __name__ == "__main__":
    # balanced_input: (3 * (1 + 3)) + ((5 * 7) + (9 / 2))
    # unbalanced_input: ((5 + 2) * ((10 + 4) * (55 + 5))
    print("\nSimple Balanced Parentheses Checker")
    print("=" * len("Simple Balanced Parentheses Checker"))
    exp_string = input("Enter the expression with parentheses: ").rstrip()
    if is_balanced(exp_string):
        print("\nParentheses in the expression are balanced.\n")
    else:
        print("\nParentheses in the expression are not balanced.\n")
