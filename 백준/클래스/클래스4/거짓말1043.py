#
#
# def main():
#     n, m = map(int, input().split())
#     info = [[0 for _ in range(n+1)] for _ in range(m+1)]
#
#     initial_info = list(map(int, input().split()))
#     if initial_info[0] != 0:
#         for member in initial_info[1:initial_info[0]+1]:
#             info[0][member] = 1
#     else:
#         print(m)
#         return
#
#     for party in range(1, m+1):
#         temp_lst = list(map(int, input().split()))
#         temp_mem = temp_lst[1:temp_lst[0]+1]
#         for mem in temp_mem:
#             info[party][mem] = 1
#
#     added_lst = list()
#     added_lst.append(info[0])
#     for idx in range(1, len(info)):
#         for pair in zip(info[idx], info[0]):
#             if pair[0] * pair[1] == 1:
#                 added_lst.append(info[idx])
#
#     new_added_lst = list()
#     new_added_lst.append(info[0])
#     for idx in range(1, len(info)):
#         for temp_lst in added_lst:
#             flag = False
#             for pair in zip(info[idx], temp_lst):
#                 if pair[0] * pair[1] == 1:
#                     new_added_lst.append(info[idx])
#                     flag = True
#                     break
#             if flag:
#                 break
#
#     # for i in info:
#     #     print(i)
#     #
#     # print("----")
#     #
#     # for i in added_lst:
#     #     print(i)
#     #
#     # print("---")
#     #
#     # for i in new_added_lst:
#     #     print(i)
#
#     print(len(info) - len(new_added_lst))
#
#
# if __name__ == "__main__":
#     main()

"""
    set이란 자료구조에 대한 이해가 중요했던 문제
    set의 연산인 union, & 등에 대해서 알고 있었어야 했다.
    코드가 복잡해질수록 엣지 케이스를 잡기 어려워진다.
    알고리즘에 대한 논리를 작성하고, 이를 코드로 최대한 간략하게 작성해야 한다.
    그렇지 않다면 엣지 케이스가 눈에 보이질 않는다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []
print(knowList)

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)
