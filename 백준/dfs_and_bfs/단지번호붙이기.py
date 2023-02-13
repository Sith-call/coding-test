from collections import deque

alist : list
visited: list
n: int

class Node:
    def __init__(self, y, x, level=1):
        self.y = y
        self.x = x
        self.level = level

def dfs(node : Node):
    pass

def bfs(node : Node):
    global n, alist, visited
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    count = 1

    if alist[node.y][node.x] == 0:
        return 0

    if visited[node.y][node.x] == 1:
        return 0

    q = deque()
    q.append(node)
    visited[node.y][node.x] = 1

    while len(q) != 0:
        now = q.popleft()

        for i in range(4):
            
            nx = now.x + dx[i]
            ny = now.y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            if alist[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue
            
            q.append(Node(ny, nx, now.level+1))
            visited[ny][nx] = 1
            count +=1

    return count

def main():
    """
    첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
     그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
    """
    global n, alist, visited
    n = int(input())

    answer = []

    alist = []

    for _ in range(n):
        row = list(map(int, input()))
        alist.append(row)

    visited = [[0 for _ in range(n)] for _ in range(n)]

    group = 0
    for i in range(n):
        for j in range(n):
        
            count = bfs(Node(i,j))
            if count != 0:
                group += 1
                answer.append(count)
                answer.sort()

    print(group)
    for i in range(len(answer)):
        print(answer[i])

if __name__ == "__main__":
    main()