

def solution(a, b):
    """
    첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
    """
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)


if __name__ == "__main__":
    a, b = map(int, input().split(" "))

    solution(a, b)