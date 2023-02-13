from collections import deque

alist: list
visited: list
m: int
n: int

class Node:
    def __init__(self,y,x, level=1):
        self.y = y
        self.x = x
        self.level = level

def dfs(start: Node): # dfs는 함수의 스택 프레임을 이용한다! 자료구조를 사용하지 않음
    global alist, visited, m, n

    if alist[start.y][start.x] == 0:
        return 0
    if visited[start.y][start.x] == 1:
        return 0

    visited[start.y][start.x] = 1

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    for i in range(4):

        ny = start.y + dy[i]
        nx = start.x + dx[i]

        if nx >= m or ny >= n or nx < 0 or ny < 0:
            continue

        if alist[ny][nx] == 0:
            continue

        if visited[ny][nx] == 1:
            continue
        
        dfs(Node(ny, nx, start.level + 1))

    return start.level
    

def bfs(start:Node):
    global alist, visited, m, n

    if alist[start.y][start.x] == 0:
        return 0
    if visited[start.y][start.x] == 1:
        return 0

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    count = 1

    q = deque()
    visited[start.y][start.x] = 1
    q.append(start)

    while len(q) != 0:

        now = q.popleft()

        for i in range(4):
            
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            
            if alist[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny,nx))
            visited[ny][nx] = 1
            count += 1

    return count

def main():
    """
    입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
    그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 
    추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
    그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
    그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
    두 배추의 위치가 같은 경우는 없다.
    """
    global alist, visited, m, n

    t = int(input())

    answer_list = []

    for _ in range(t):

        answer = 0

        m, n, k = map(int, input().strip().split())

        alist = [[0 for _ in range(m)] for _ in range(n)]

        visited = [[0 for _ in range(m)] for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().strip().split())
            alist[y][x] = 1

        for i in range(m):
            for j in range(n):
                count = dfs(Node(j,i))
                if count != 0:
                    answer+=1
        
        answer_list.append(answer)

    for value in answer_list:
        print(value)


if __name__ == "__main__":
    main()