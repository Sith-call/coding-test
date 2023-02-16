from queue import PriorityQueue
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    q = PriorityQueue()
    answer = 0
    for _ in range(n):
        q.put(int(input()))

    while q.qsize() > 1:
        num1 = q.get()
        num2 = q.get()
        answer += num1+num2
        q.put(num1+num2)

    print(answer)


if __name__ == "__main__":
    main()