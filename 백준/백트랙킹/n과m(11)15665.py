
numbers:set
answer:list = []
n:int
m:int

def backtracking(count):
    global numbers, answer, n, m
    if count == m:
        print(*answer)
        return
    for i in numbers:
        answer.append(i)
        backtracking(count+1)
        answer.pop()


def main():
    global numbers, answer, n, m
    n, m = map(int, input().split())
    numbers_set = set(map(int,input().split()))
    numbers = list(numbers_set)
    numbers.sort()

    print(numbers)

    backtracking(0)



if __name__ == "__main__":
    main()