

def solution(a, b):
    data = a + b
    print(data)


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split(" "))
        solution(a, b)
