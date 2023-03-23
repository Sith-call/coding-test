"""
    그리디 문제를 푸는 방법의 핵심
    1. 오름차순 또는 내림차순의 기준이 문제에서 제시된다.
    2. 탐욕법을 통해 얻은 답은 최적해를 보장하지 않는다.
    3. 탐욕법을 통해 얻은 답을 검증할 수 있어야 답으로 확실할 수 있다.

"""


def solution():
    pass


def main():
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[0:n]
    answer = 0

    numbers.sort(reverse=True)

    num1 = numbers[0]
    num2 = numbers[1]

    if num1 == num2:
        answer = num1 * m
    else:
        count = 0
        for _ in range(m):
            count += 1
            if count % k == 0:
                answer += num2
            else:
                answer += num1

    print(answer)


if __name__ == "__main__":
    main()
