from collections import deque

alist : list
visited : list

def dfs(start : int):
    if visited[start] == 1:
        return

    visited[start] = 1
    print(start, end=" ")

    for node in alist[start]:
        dfs(node)

def bfs(start : int):
    global alist, visited
    q = deque()
    q.append(start)
    visited[start] = 1
    print(start, end=" ")

    while len(q) != 0 :
        node = q.popleft() 
        for n in alist[node]:
            if visited[n] == 1:
                continue
            q.append(n)
            visited[n] = 1
            print(n, end=" ")


def main():
    """
    첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
    입력으로 주어지는 간선은 양방향이다.
    """
    global alist, visited
    n, m, v = map(int, input().strip().split())

    alist = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for _ in range(m):
        s, e = map(int, input().strip().split())
        alist[s].append(e)
        alist[e].append(s)
        alist[s].sort() 
        alist[e].sort()


    print(alist)

    dfs(v)
    visited = [0] * (n+1)
    print()
    bfs(v)


if __name__ == "__main__":
    main()