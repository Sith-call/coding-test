
numbers:list = []
n:int
m:int
answer:list = []
visited:list = []

def backtracking(count):
    global numbers, n, m, answer, visited
    if count == m:
        print(*answer)
        return
    for i in numbers:
        if visited[i] == 1:
            continue
        answer.append(i)
        visited[i] = 1
        backtracking(count+1)
        answer.pop()
        visited[i] = 0

def main():
    global numbers, n, m, answer, visited
    n, m = map(int, input().split())
    numbers = list(map(int,input().split()))
    numbers.sort()
    visited = [0] * (10**4)

    backtracking(0)
    

if __name__ == "__main__":
    main()