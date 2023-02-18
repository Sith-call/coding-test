import sys
import heapq

n = int(sys.stdin.readline())

left_heap = []
right_heap = []
answer = []

for i in range(n):
    input_num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-input_num, input_num))
    else:
        heapq.heappush(right_heap, (input_num, input_num))

    if right_heap and left_heap[0][1] > right_heap[0][0]:
        min = heapq.heappop(right_heap)[0]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))

    answer.append(left_heap[0][1])

for j in answer:
    print(j)