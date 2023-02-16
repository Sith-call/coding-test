from queue import PriorityQueue
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ops = []
    # 부호에 따라 큐를 나누지만 절댓값만 저장한다. 부호의 의미는 큐에 부여한다.
    q_pos = PriorityQueue()
    q_neg = PriorityQueue()

    for _ in range(n):
        ops.append(int(input()))

    for op in ops:
        if op == 0:
            # 큐가 모두 비어있는 경우를 처리한다.
            #   큐가 모두 비워져 있는 경우 0을 출력한다.
            if q_pos.empty() and q_neg.empty():
                print(0)

            # 둘 중에 하나만 비어있는 경우를 처리한다.
            #   양수큐만 채워져 있는 경우 그대로 출력한다.
            #   음수큐만 채워져 있는 경우 부호를 바꿔서 출력한다
            elif not q_pos.empty() and q_neg.empty():
                print(q_pos.get())
            elif q_pos.empty() and not q_neg.empty():
                print((-1)*q_neg.get())

            # 큐가 모두 비워져 있지 않은 경우를 처리한다.
            #   큐의 가장 앞에 있는 원소의 절댓값을 서로 비교하고 둘 중 하나만 출력한다.
            #   출력하지 않은 원소는 복귀시킨다.
            #   비교 기준
            #   1. 절댓값이 작은 것을 출력한다.
            #   2. 절댓값이 같다면 음수를 먼저 출력한다.
            else:
                value_pos = q_pos.get()
                value_neg = q_neg.get()
                if value_neg == value_pos:
                    print((-1)*value_neg)
                    q_pos.put(value_pos)
                elif value_neg > value_pos:
                    print(value_pos)
                    q_neg.put(value_neg)
                else:
                    print((-1)*value_neg)
                    q_pos.put(value_pos)
        else:
            # 음수가 들어온 경우를 처리한다.
            if op < 0:
                # 절댓값으로 저장한다.
                q_neg.put((-1)*op)
            # 양수가 들어온 경우를 처리한다.
            else :
                q_pos.put(op)

if __name__ == "__main__":
    main()