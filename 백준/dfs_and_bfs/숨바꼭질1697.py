from collections import deque

visited: list
k: int
q: deque
max_value: int

def dfs():
    pass

def bfs(start: int):
    """
    이 문제의 핵심은 bfs에서 발생하는 자식 노드들을 내가 커스텀할 수 있다는 것이다.
    그리고 이 노드의 depth가 곧 원하는 지점까지 접근하는 시간이 된다.
    매우 유익한 문제!
    이때 depth를 측정하기 위해서 visited 리스트를 활용한다.
    """
    global visited, k, q, max_value
    q = deque()
    q.append(start)

    while len(q) != 0:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            if (nx >= 0 and nx <= max_value) and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1


    pass

def main():
    """
    첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
    """
    global visited, k, q, max_value
    n, k = map(int, input().split())
    max_value = 100000
    visited = [0] * (max_value + 1)
    answer = bfs(n)
    print(answer)

if __name__ == "__main__":
    main()