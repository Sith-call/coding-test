
"""
    명확한 알고리즘이 떠오르지 않는다면 브루트포스로 간다~!
    지금은 최단 거리를 구하는 문제이므로, bfs로 푼다.
"""
import sys
from collections import deque
import copy

input = sys.stdin.readline

alist: list
visited: list


class Node:
    def __init__(self, num, level=0):
        self.num = num
        self.level = level


def bfs(node: Node, e) -> int:
    global alist, visited

    q = deque()
    q.append(node)
    visited[node.num] = 1

    while len(q) != 0:
        now_node = q.popleft()
        for n in alist[now_node.num]:
            if n == e:
                # print(f"{node.num} {e} {now_node.level + 1}")
                return now_node.level + 1
            if visited[n] == 1:
                continue
            q.append(Node(n, now_node.level+1))
            visited[n] = 1


def main():
    global alist, visited
    n, m = map(int, input().split())
    alist = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        if s in alist[e] or e in alist[s]:
            continue
        alist[s].append(e)
        alist[e].append(s)

    distances = dict()

    for s in range(1, n+1):
        temp_distances = []
        for e in range(1, n+1):
            if s == e:
                continue
            visited = [0] * (n+1)
            temp_distances.append(bfs(Node(s), e))
        distances[s] = sum(temp_distances)

    min_value = distances[1]
    target = 1
    for friend in distances.keys():
        if min_value > distances[friend]:
            min_value = distances[friend]
            target = friend

    print(target)


if __name__ == "__main__":
    main()
