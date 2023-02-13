from collections import deque

alist : list
visited: list

def bfs(start:int):
    global visited, alist
    if visited[start] == 1:
        return 0
    count = 0
    q = deque()
    q.append(start)
    visited[start] = 1

    while len(q) != 0:
        now = q.popleft()
        for node in alist[now]:
            if visited[node] == 1:
                continue
            q.append(node)
            visited[node] = 1
            count+=1

    return count



def dfs():
    pass

def main():
    """
    첫째 줄에 연결 요소의 개수를 출력한다.
    """
    global visited, alist
    n, m = map(int, input().split())
    answer = 0

    alist = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        alist[s].append(e)
        alist[e].append(s)

    for i in range(1,n+1): # 노드를 기준으로 순회, 시작 노드 체크
        if bfs(i) != 0:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()