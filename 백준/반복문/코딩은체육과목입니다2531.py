

def solution(n):
    cnt = n // 4
    string = "int"
    for _ in range(cnt):
        string = "long " + string
    print(string)


if __name__ == "__main__":
    n = int(input())
    solution(n)
