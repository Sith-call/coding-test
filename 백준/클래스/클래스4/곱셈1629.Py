"""
    수학적인 지식을 통해 알고리즘을 하나의 수식으로 표현해낼 수 있을 것 같은 느낌이 든다.
    a^b = k*c + answer (0 <= answer < c)

    a = x * c + y
    y = a - x*c
    y = a % c
    a^2 = xc^2 + 2xc + y^2
        = (x*c)^2 + 2*x*c*y + y^2

    a = x * c + y

    y^2 = k * c + z   answer = z ** (log2(b))

    z^2 = k' * c + z'  answer = z' ** log2(log2b)

    10 = 12 * 0 + 10 answer = 10**11 % 12

    10^2 = 12*8 + 4 answer = 4**(11/2) % 12
    => 여기서 수식에 루트가 생겨서 예상대로 알고리즘이 실행되지 않는다.
    => 내가 원하는대로 갈려면 2의 배수로서 b가 주어져야 한다.

    4^2 = 12*1 + 4 answer = 4**log2(log2(11)) % 12

    https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

"""
import math
import sys
# input = sys.stdin.readline()


# def main():
#     a, b, c = map(int, input().split())
#     while math.log2(b) > 0:
#         a, b, c = (a % c) ** 2, math.log2(b), c
#     answer = (a % c) ** b
#     print(answer)
#
#
# if __name__ == "__main__":
#     main()

import sys

a, b, c = map(int, sys.stdin.readline().split())


def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))::wqqw

# 재귀함수를 이용한다.