"""
Created on: 22-Mar-2018
Created by: Maneesh D
"""
from __future__ import absolute_import
from Stack import Stack


def integer_to_binary_converter(integer: int) -> str:
    """Converts an integer into its binary form"""
    if integer == 0 or integer == 1:
        return str(integer)
    elif integer < 0:
        return "! Only supports positive integers !"

    rem_stack = Stack(100)
    while integer > 0:
        rem = integer % 2
        ret = rem_stack.push(rem)
        if ret is False:
            return "!!! ERROR !!!"
        integer //= 2

    binary_string = ""
    while not rem_stack.is_empty():
        popped_item = rem_stack.pop()
        if popped_item is not False:
            binary_string += str(popped_item)

    return binary_string


if __name__ == "__main__":
    app_title = "integer to binary converter"
    print()
    print(app_title.title())
    print("=" * len(app_title))
    valid_input = False
    int_num = None
    while not valid_input:
        try:
            int_num = input("Enter the integer (Ctrl+C to exit): ")
            int_num = int(int_num.strip())
            break
        except KeyboardInterrupt:
            print("Got Ctrl+C...\nExiting...")
            exit(1)
        except ValueError:
            print("\n!!! Enter a valid decimal number !!!\n")
            continue
        except Exception as exp:
            print(exp)
    int_num_binary = integer_to_binary_converter(int_num)
    print()
    print(int_num, "in binary:", int_num_binary, "\n")
