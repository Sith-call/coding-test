from collections import deque

alist : list
visited: list

def bfs(start:int):
    global visited, alist
    if visited[start] == 1:
        return 0
    count = 1
    q = deque()
    q.append(start)
    visited[start] = 1 # 그냥 섬처럼 떠 있는 노드도 하나의 연결요소로 봐야함.

    while len(q) != 0:
        now = q.popleft()
        for node in alist[now]:
            if visited[node] == 1:
                continue
            q.append(node)
            visited[node] = 1
            count+=1

    return count



def dfs(start: int):
    global visited, alist # dfs는 함수를 몇 번 실행시킬 수 있는지를 기준으로 연결 요소를 센다
    if visited[start] == 1:
        return
    visited[start] = 1
    for node in alist[start]:
        if visited[node] == 1:
            continue
        dfs(node)


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

    # for i in range(1,n+1): # 노드를 기준으로 순회, 시작 노드 체크
    #     if bfs(i) != 0:
    #         answer += 1

    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()