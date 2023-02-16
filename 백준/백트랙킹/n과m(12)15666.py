numbers:set
answer:list = []
n:int
m:int

def backtracking(count, start):
    global numbers, answer, n, m
    if count == m:
        print(*answer)
        return
    for i in numbers:
        if i >= start:
            answer.append(i)
            backtracking(count+1, i)
            answer.pop()

    pass

def main():
    global numbers, answer, n, m
    n, m = map(int, input().split())
    numbers_set = set(map(int,input().split()))
    numbers = list(numbers_set)
    numbers.sort()

    backtracking(0, 0)


if __name__ == "__main__":
    main()