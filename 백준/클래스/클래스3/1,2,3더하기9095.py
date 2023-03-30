import sys
input = sys.stdin.readline

"""
    n이 11까지 주어졌다.
    즉, 구현에 해당하는 브루트 포스가 가능하다는 뜻이다.
    이런 경우에는 망설임 없이 구현을 적용시켜본다.
"""
def factorial(n: int) -> int:
    if n == 0:
        return 1
    value = 1
    while n > 0:
        value *= n
        n -= 1
    return value

def main():
    n = int(input())
    lst = []

    for _ in range(n):
        lst.append(int(input()))

    answers = []
    for num in lst:
        answer = 0
        for i in range(num+1):
            for j in range(num+1):
                for k in range(num+1):
                    if num == ((i * 1) + (j * 2) + (k * 3)):
                        answer += ((factorial(i+j+k))/(factorial(i) * factorial(j) * factorial(k)))
        answers.append(answer)

    for answer in answers:
        print(int(answer))


if __name__ == "__main__":
    main()
