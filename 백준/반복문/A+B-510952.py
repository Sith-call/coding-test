import sys


if __name__ == "__main__":
    i = 0
    while True:
        try:
            a, b = map(int, sys.stdin.readline().rstrip().split(" "))
            print(f"{a + b}")
            i += 1
        except:
            break

