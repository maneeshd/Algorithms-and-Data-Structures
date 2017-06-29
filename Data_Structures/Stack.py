"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 24/6/17

Stack
"""


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, data):
        if len(self.stack) > 10:
            print("!!! Stack Overflow !!!\n")
            return
        self.top += 1
        self.stack.append(data)
        print("%d pushed into stack..." % data)

    def pop(self):
        if self.top < 0:
            print("!!! Stack is Empty !!!\n")
            return
        data = self.stack[self.top]
        self.top -= 1
        return data

    def display_stack(self):
        i = len(self.stack) - 1
        while i > -1:
            print("\t\t%d" % self.stack[i])
            i -= 1
        print()

if __name__ == '__main__':
    print("Stack Operation")
    print("-" * len("Stack Operation"))
    stak = Stack()
    while True:
        print("1. Push\n"
              "2. Pop\n"
              "3. Display\n"
              "4. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            dat = int(input("Enter the number to push: "))
            stak.push(dat)
        elif choice == "2":
            dat = stak.pop()
            if dat:
                print("Popped element is: %d\n" % dat)
        elif choice == "3":
            print("Stack: ")
            stak.display_stack()
        elif choice == "4":
            exit(0)
        else:
            print("Enter a valid choice !!")
