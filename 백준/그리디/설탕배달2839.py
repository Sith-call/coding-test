"""
    n의 최대값이 5000이기 때문에 o(n^2)의 시간복잡도를 가지는 완전 탐색으로
    문제를 해결하려고 한다. 그리디는 최적해를 보장하지 않기 때문이다.
"""


def main():
    n = int(input())
    count_3 = n // 3
    count_5 = n // 5

    if count_3 == 0 and count_5 == 0:
        print(-1)
    elif count_3 != 0 and count_5 == 0:
        if n % 3 == 0:
            print(n//3)
        else:
            print(-1)
    elif count_3 == 0 and count_5 != 0:
        if n % 5 == 0:
            print(n // 5)
        else:
            print(-1)
    else:  # count_3 != 0 and count_5 != 0
        answer = []
        for i in range(count_3+1):
            for j in range(count_5+1):
                if n == 3 * i + 5 * j:
                    answer.append(i+j)
        if len(answer) != 0:
            print(min(answer))
        else:
            print(-1)


if __name__ == "__main__":
    main()
