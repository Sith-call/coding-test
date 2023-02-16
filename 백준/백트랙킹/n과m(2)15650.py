n: int
m: int
visited: list
answer:list = []
memory:list = []

def backtracking(count):
    global visited, visited2, n, m, answer
    if count == m:
        temp_set = set(answer)
        if temp_set in memory:
            return
        memory.append(temp_set)
        print(*answer)
        return 
    for i in range(1,n+1):
        if i in memory:
            continue
        if visited[i] == 0:
            visited[i] = 1
            answer.append(i)
            backtracking(count+1)
            visited[i] = 0
            answer.pop()


def main():
    """
    첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
    """
    global visited, n, m, answer
    n, m = map(int, input().split())

    visited = [0] * (n+1)

    backtracking(0)


if __name__ == "__main__":
    main()