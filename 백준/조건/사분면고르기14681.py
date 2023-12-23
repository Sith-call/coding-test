

def solution(a, b):
    if (a > 0) and (b > 0):
        print(1)
    elif (a > 0) and (b < 0):
        print(4)
    elif (a < 0) and (b > 0):
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    solution(a, b)
