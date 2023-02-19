from collections import deque

n: int
m: int
visited: list


class Node:
    def __init__(self, y, x, level=1):
        self.y = y
        self.x = x
        self.level = level


def bfs(start: Node, maps: list):
    global n, m, visited
    answer = []

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque()
    q.append(start)
    visited[start.y][start.x] = 1

    while len(q) != 0:
        now = q.popleft()

        if now.x == n - 1 and now.y == m - 1:
            answer.append(now.level)

        for i in range(4):

            nx = now.x + dx[i]
            ny = now.y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            if maps[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny, nx, now.level + 1))
            visited[ny][nx] = 1

    if len(answer) != 0:
        return min(answer)
    else:
        return -1


def solution(maps):
    global n, m, visited

    m = len(maps)
    n = len(maps[0])

    visited = [[0 for _ in range(n)] for _ in range(m)]

    return bfs(Node(0, 0), maps)


def main():
    maps = [[1, 1, 1, 1], [1, 1, 1, 1]]
    print(solution(maps))


if __name__ == "__main__":
    main()