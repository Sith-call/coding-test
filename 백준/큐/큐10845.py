from collections import deque


def main():
    q = deque
    n = int(input())
    for _ in range(n):
        value = 0
        op, value = input().split()
        print(op)
        print(value)


if __name__ == "__main__":
    main()