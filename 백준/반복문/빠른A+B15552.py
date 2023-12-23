import sys


def solution(a, b):
    print(a + b)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        solution(a, b)
