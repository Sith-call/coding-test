
answer:list = []
numbers:list
n:int
m:int

def backtracking(count:int):
    global answer, numbers, n, m
    if count == m :
        print(*answer)
        return
    for i in numbers:
        answer.append(i)
        backtracking(count+1)
        answer.pop()

def main():
    global answer, numbers, n, m
    n, m = map(int, input().split())
    numbers = list(map(int,input().split()))
    numbers.sort()

    backtracking(0)


if __name__ == "__main__":
    main()