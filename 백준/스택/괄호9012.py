import sys
input = sys.stdin.readline


def solution(data: str):
    stack = []
    for datum in data:
        if datum == "(":
            stack.append(datum)
        if (datum == ")") and (len(stack) != 0) and (stack.pop() == "("):
            continue
        if (datum == ")") and (len(stack) == 0):
            return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


def main():
    answer = []
    n = int(input())
    for _ in range(n):
        data = input()
        answer.append(solution(data))

    for output in answer:
        print(output)


if __name__ == "__main__":
    main()
    