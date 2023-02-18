import heapq
import sys
input = sys.stdin.readline


def add_list(n_list:list,num):
    if not num in n_list:
        n_list.append(num)

def main():
    n, m = map(int, input().split())
    s_heap = []
    e_heap = []
    alist = [[] for _ in range(n+1)]
    answer = []
    visited = [0] * (n+1)

    for _ in range(m):
        s, e = map(int, input().split())
        heapq.heappush(s_heap, s)
        alist[s].append(e)

    while s_heap or e_heap:
        if not len(s_heap) == 0 and not len(e_heap) == 0:
            if e_heap[0] <= s_heap[0]:
                add_list(answer, heapq.heappop(e_heap))
                continue
            else:
                num = heapq.heappop(s_heap)
                e_heap = e_heap + alist[num]
                add_list(answer, num)
                continue
        if not len(s_heap) == 0 and len(e_heap) == 0:
            num = heapq.heappop(s_heap)
            e_heap = e_heap + alist[num]
            heapq.heapify(e_heap)
            add_list(answer, num)
            continue
        if len(s_heap) == 0 and not len(e_heap) == 0:
            for value in e_heap:
                add_list(answer, value)
            e_heap = []
            continue

    print(*answer)


if __name__ == "__main__":
    main()