
n:int
m:int
answer:list = []


def backtracking(count, start):
    global n, m, answer
    if count == m:
        print(*answer)
        return
    for i in range(start,n+1):
        answer.append(i)
        backtracking(count+1,i)
        answer.pop()

def main():
    global n, m, answer
    n, m = map(int,input().split())

    backtracking(0,1)

if __name__ == "__main__":
    main()