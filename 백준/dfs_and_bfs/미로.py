from collections import deque


maze: list
visited: list
n: int
m: int

class Node:
    def __init__(self, y, x, level=1):
        self.y = y
        self.x = x
        self.level = level


def bfs(node : Node):
    global n, m, visited, maze

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append(node)
    visited[node.y][node.x] = 1

    while len(q) != 0:
        now = q.popleft()

        if now.x == m-1 and now.y == n-1 :
            return now.level

        for i in range(4):

            nx = now.x + dx[i]
            ny = now.y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if maze[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny,nx, now.level+1))
            visited[ny][nx] = 1

    return -1

def main():
    """
    첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
    다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
    각각의 수들은 붙어서 입력으로 주어진다.
    """
    global n, m, visited, maze

    n, m = map(int, input().strip().split())

    visited = [[0 for _ in range(m)] for _ in range(n)]
    maze = []

    for _ in range(n):
        row = list(map(int, input()))
        maze.append(row)

    answer = bfs(Node(0,0))

    print(answer)

if __name__ == "__main__":
    main()