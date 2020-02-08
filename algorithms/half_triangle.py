if __name__ == "__main__":
    # Prints Half Triangle
    for i in range(5):
        for _ in range(i):
            print("*", end=" ")
        print("")
    for i in range(5, 0, -1):
        for _ in range(i):
            print("*", end=" ")
        print("")
    print("")
