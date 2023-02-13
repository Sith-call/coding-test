from collections import deque

alist: int
visited: int
q: deque
m: int
n: int

class Node:
    def __init__(self,y,x):
        self.y = y
        self.x = x

def dfs():
    """
    이 문제는 bfs가 적합하다.
    depth의 값이 곧 정답인 문제인데, dfs로 탐색하면 depth 값이 정답과 다른 경우가
    발생할 수 있다.
    """
    pass

def bfs():
    """
    큐에 하나의 노드가 아닌 여러 개의 노드가 들어가는 문제!
    depth를 누적시키고, 이것의 최대값을 구하기 위해선, visited 또는 alist에 값을 누적해서 기록시킨다.
    """
    global alist, visited, q, m, n

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    while len(q) != 0:
        now = q.popleft()
        
        for i in range(4):
             ny = now.y + dy[i]
             nx = now.x + dx[i]

            # if 문을 통해 조건을 filtering할 수도 있고, targeting할 수도 있다.
             if (nx >= 0 and nx < m) and (ny >= 0 and ny < n) and (alist[ny][nx] == 0) and (visited[ny][nx] == 0): # targeting
                q.append(Node(ny,nx))
                visited[ny][nx] = visited[now.y][now.x] + 1


def main():
    """
    첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. 
    M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
    단, 2 ≤ M,N ≤ 1,000 이다. 
    둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
    즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
    하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
    정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 
    정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
    """
    global alist, visited, q, m, n
    m, n = map(int, input().strip().split())

    q = deque()

    alist = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        row = list(map(int, input().split()))
        alist.append(row)

    for i in range(m):
        for j in range(n):
            if alist[j][i] == 1:
                q.append(Node(j,i))
                visited[j][i] = 1

    bfs()

    # 이미 모든 토마토가 익은 경우
    count = 0
    for i in range(m):
        for j in range(n):
            if alist[j][i] == -1 or alist[j][i] == 1:
                count += 1
    if count == m*n:
        print(0)
        return

    # 익지 않은 토마토가 있는 경우
    for i in range(m):
        for j in range(n):
            if visited[j][i] == 0 and alist[j][i] == 0:
                print(-1)
                return

    # 시간이 걸려 토마토가 전부 익은 경우
    answer = 0
    for i in range(m):
        for j in range(n):
            if visited[j][i] > answer:
                answer = visited[j][i]
    print(answer-1)

if __name__ == "__main__":
    main()