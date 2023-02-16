n:int
m:int
answer : list = []

def backtracking(count):
    global n, m, answer
    if count == m:
        print(*answer)
        return 
    for i in range(1,n+1):
        answer.append(i)
        backtracking(count+1)
        answer.pop()

def main():
    global n, m

    n,m = map(int, input().split())

    backtracking(0)

if __name__ == "__main__" :
    main()