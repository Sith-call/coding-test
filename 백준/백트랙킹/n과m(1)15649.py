
visited: list
n: int
m : int
answer: list = []

def backtracking(count):
    global visited, n, m, answer
    if count == m:
        print(*answer)
        return
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            answer.append(i)
            backtracking(count+1)
            visited[i] = 0
            answer.pop()
        

def main():
    global visited, n, m
    n, m = map(int, input().split())
    
    visited = [0] * (n+1)

    backtracking(0)

if __name__ == "__main__":
    main()
