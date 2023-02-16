from queue import PriorityQueue
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ops = []
    q = PriorityQueue() # 최소힙으로만 사용할 수 있기 때문에 최대힙으로 사용할 때는 부호를 바꿔서 넣어준다

    for _ in range(n):
        ops.append(int(input()))
    
    for op in ops:
        if op == 0:
            if q.empty():
                print(0)
            else:
                print((-1)*q.get())
        else:
            q.put((-1)*op)


if __name__ == "__main__":
    main()