


"""
    정확하게 들어맞는 알고리즘이 떠오르지 않는다.
    아니다. 백트래킹 또는 bfs을 통해 문제를 푼다.
    연산을 통해 어떤 수에 도달하는 문제 푼 적이 있다.
"""
import sys
from collections import deque
input = sys.stdin.readline


visited: list


# class Node:  # 그래프 상의 노드에 필요한 데이터가 2개 이상이 경우 클래스를 통해 묶는다.
#     def __init__(self, val, level=0):
#         self.val = val
#         self.level = level
# 노드 클래스를 사용하는 경우에는 파이썬이 상당히 느리다!!!
# 그래서 웬만하면 사용하지 말자.

def bfs(n: int):
    global visited
    q = deque()
    q.append(n)

    while len(q) != 0:
        now_node = q.popleft()

        # 여기서 중요! 연산의 순서를 정해야 한다.
        # 큰 수로 나눠야 제일 빨리 작아진다. 고로 3부터 적용시킨다.
        # 빼는 연산은 임팩트가 작기 때문에 나중에 적용시킨다.
        # 그리고 시작이 1보다 크기 때문에 3 -> 2 -> 1 순으로 적용시킨다. (그래프로 확인 가능)

        if now_node == 1:
            return visited[now_node]
        if now_node % 3 == 0 and visited[now_node//3] == 0:
            q.append(now_node // 3)
            visited[now_node//3] = visited[now_node] + 1
        if now_node % 2 == 0 and visited[now_node//2] == 0:
            q.append(now_node // 2)
            visited[now_node // 2] = visited[now_node] + 1
        if visited[now_node - 1] == 0:
            q.append(now_node - 1)
            visited[now_node - 1] = visited[now_node] + 1


def main():
    global visited
    n = int(input())
    visited = [0] * (n+1)
    answer = bfs(n)
    print(answer)


if __name__ == "__main__":
    main()
