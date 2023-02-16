
answer:list = []
numbers:list
n:int
m:int

def backtracking(count,start):
    global answer, numbers, n, m
    if count == m:
        print(*answer)
        return
    for i in numbers:
        if i >= start:
            answer.append(i)
            backtracking(count+1,i)
            answer.pop()

def main():
    global answer, numbers, n, m
    n,m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    backtracking(0,numbers[0])

if __name__ == "__main__":
    main()