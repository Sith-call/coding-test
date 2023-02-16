
answer:list = []
numbers:list
visited:list 
n:int
m:int

def backtracking(count):
    global answer, numbers, n, m, visited
    remember_me = 0 # 이 변수를 통해서 초반에 필요한 경우를 필터링함 from : https://honggom.tistory.com/111
    if count == m:
        print(*answer)
        return
    for i in range(len(numbers)):
            if visited[i] == 0 and ( remember_me != numbers[i] ):
                answer.append(numbers[i])
                visited[i] = 1
                remember_me = numbers[i]
                backtracking(count+1)
                answer.pop()
                visited[i] = 0


def main():
    global answer, numbers, n, m, visited
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    visited = [0] * (n)

    backtracking(0)

if __name__ == "__main__":
    main()

"""
    [초기 버전]
answer:list = []
numbers:list
memory:list = []
visited:list 
n:int
m:int

def backtracking(count):
    global answer, numbers, memory, n, m, visited
    if count == m and (not answer in memory): 
        print(*answer)
        memory.append(list(answer))
        return
    for i in range(len(numbers)):
            if visited[i] == 0:
                answer.append(numbers[i])
                visited[i] = 1
                backtracking(count+1)
                answer.pop()
                visited[i] = 0


def main():
    global answer, numbers, memory, n, m, visited
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    visited = [0] * (n)

    backtracking(0)

if __name__ == "__main__":
    main()
"""

"""
    [고찰]
    in 연산자는 파이썬에서 자료구조마다 다른 시간 복잡도를 가진다.

    > list, tuple
        Average : O(n)
        하나하나 순회하기 때문에 O(n)만큼의 시간복잡도를 갖는다

    >set, dictionary
        Average : O(1), Worst : O(n)
        내부적으로 hash를 통해 저장하므로 접근하는 시간은 O(1)이다. 하지만 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)이 걸릴 수도 있다.

    나는 초기 버전에서 in 연산자를 통해서 중복을 걸러냈다.
    그러나 이렇게 된다면 for문을 통해서 전체 순회를 하게 된다.
    그래서 애초에 처음 순회를 돌 때 조건을 추가해서 초반에 필터링을 해줘야 한다.
    이렇게 바꾸고 나니 시간 초과가 사라졌다.
"""