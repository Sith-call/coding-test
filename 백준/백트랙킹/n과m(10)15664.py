
numbers:list
answer:list = []
n:int
m:int

def backtracking(count,start):
    global n, m, numbers, answer
    if count == m:
        print(*answer)
        return
    remember_me = 0
    for i in range(len(numbers)):
        if i > start and remember_me != numbers[i]:
            answer.append(numbers[i])
            remember_me = numbers[i]
            backtracking(count+1, i)
            answer.pop()

def main():
    global n, m, numbers
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    backtracking(0,-1)


if __name__ == "__main__":
    main()