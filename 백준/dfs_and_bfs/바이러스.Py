alist : list
visited : list

def dfs(start : int):
    global alist, visited
    if visited[start] == 1:
        return
    visited[start] = 1
    for node in alist[start]:
        dfs(node)

def main():
    """
    (입력)
    첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 
    1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 
    있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 
    상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
    """
    global alist, visited
    n = int(input())
    e = int(input())

    alist = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(e):
        s, e = map(int, input().strip().split())
        alist[s].append(e)
        alist[e].append(s)

    dfs(1)
    print(visited.count(1)-1)


if __name__ == "__main__":
    main()