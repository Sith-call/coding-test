"""
    문제의 로직은 아주 간단한 순열이다.
    그러나 시간 복잡도와 공간 복잡도를 낮춰야만 한다.
    그렇게 하기 위해서 주어진 문제를 함축적인 수학 공식으로 표현해본다.

    모든 경우의 수는 일단 n개의 군으로 나뉜다.
    그리고 각각의 군은 다시 n개의 군으로 다시 나뉜다.
    즉, 트리 구조를 띈 형태로 순서가 존재하는 것이다.

    그렇다면 이를 트리 구조로 곧이곧대로 구현할 것인가?
    노드의 개수는 n!개가 필요하다. 순열을 이용한 것에서 전혀 복잡도가 낮아지지 않았다.

    그러나 트리 구조를 띈다는 것을 이용해서 수학 공식을 추론해본다.
    일단 작은 스케일에서 추론해본다.

    n=1
    (1, )

    n = 2
    (1, 2)
    (2, 1)

    n = 3, k = 5

    [1, 2, 3]
    [1, 3, 2]

    [2, 1, 3]
    [2, 3, 1]

    [3, 1, 2]
    [3, 2, 1]

    5 = 2*2 + 1

    n = 4, k = 15

    (1, 2, 3, 4)
    (1, 2, 4, 3)
    (1, 3, 2, 4)
    (1, 3, 4, 2)
    (1, 4, 2, 3)
    (1, 4, 3, 2)

    (2, 1, 3, 4)
    (2, 1, 4, 3)
    (2, 3, 1, 4)
    (2, 3, 4, 1)
    (2, 4, 1, 3)
    (2, 4, 3, 1)

    (3, 1, 2, 4)

    (3, 1, 4, 2)

    (3, 2, 1, 4)
    (3, 2, 4, 1)

    (3, 4, 1, 2)
    (3, 4, 2, 1)

    (4, 1, 2, 3)
    (4, 1, 3, 2)
    (4, 2, 1, 3)
    (4, 2, 3, 1)
    (4, 3, 1, 2)
    (4, 3, 2, 1)

    15 = (4-1)!*3(18) - (4-2)!*2(4) + (4-3)!*1(1) - (4-4)!*4(0) (마지막은 안 쓴 수를 넣으면 됨)
    (3, 2, 1, 4)

    규칙을 찾았다! -> 그러나 팩토리얼 연산 때문에 적용하기 어렵다.
    lst = []
    lst.append(k//(n-1)! + 1)
    k = k % (n-1)!
    ...
    if (n-i)! == 0!
        종료


"""

from itertools import permutations as pm


def solution_by_permutation(n, k):
    n = 2
    answer = list(pm(list(range(1, n + 1)), n))
    answer.sort()
    return list(answer[k - 1])


import sys

sys.setrecursionlimit(10 ** 8)

cache = dict()


def factorial(n):
    if n in cache.keys():
        return cache[n]
    else:
        result = n * factorial(n - 1)
        cache[n] = result
        return result


def solution_by_recursion(n, k):
    factorial(20)
    return
    answer = []
    visited = [0 for _ in range(n)]
    for i in range(1, n + 1):
        if k == 0:
            visited = [i + 1 for i, x in enumerate(visited) if x == 0]
            answer.append(visited[0])
            break
        answer.append((k // factorial(n - i)) + 1)
        visited[i - 1] = 1
        k = k % factorial(n - i)
    print(answer)


if __name__ == "__main__":
    solution_by_recursion(3, 5)
