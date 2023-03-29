# # 해당 채널에 도달 가능한 방법들
# # 1. + - 이용
# # 2. 번호 이용
# # 3. 1,2 섞어서 이용
# # 해당 방법들로 방법을 모두 도출한 이후에 비교한다.
# # 로직이 어렵다고 느껴진다면, 브루트포스도 괜찮은 방법이다.
# # 테케를 다 맞췄음에도 실제로 제출했을 시에는 오류가 뜰 때가 있었다.
# # 철저하게 배운 알고리즘으로 풀 수 있는게 아니라면 지양하다록 하자
#
# def solution(n: str, lst: list, pre_answer: str) -> int:
#     n_lst = list(map(int, n))
#     answer = ""
#
#     count = len(list(pre_answer))
#
#     first_target = 0
#     min_value = abs(n_lst[0] - lst[0])
#     for i in range(len(lst)):
#         if abs(n_lst[0] - lst[i]) < min_value:
#             min_value = abs(n_lst[0] - lst[i])
#             first_target = i
#
#     answer += str(lst[first_target])
#
#     if n_lst[0] > lst[first_target]:
#         for _ in range(len(n_lst) - count):
#             answer += str(max(lst))
#         return int(answer)
#     elif n_lst[0] < lst[first_target]:
#         for _ in range(len(n_lst) - count):
#             answer += str(min(lst))
#         return int(answer)
#     else:
#         new_n = ""
#         for i in n_lst[1:]:
#             new_n += str(i)
#         count += 1
#         answer += str(solution(new_n, lst, answer))
#         return int(answer)
#
#
# def main():
#     n = int(input())
#     m = int(input())
#     if m != 0:
#         unavailable_lst = list(map(int, input().split()))
#     else:
#         answer_2 = len(list(str(n)))
#         print(answer_2)
#         return
#
#     lst = list(range(10))
#
#     for i in unavailable_lst:
#         lst.remove(i)
#
#     nearest_num = solution(str(n), lst, "")
#
#     answer = []
#     answer_1 = abs(100 - n)
#     answer_3 = abs(len(list(str(nearest_num)))) + abs(n - nearest_num)
#     answer.append(answer_1)
#     answer.append(answer_3)
#
#     print(f"{answer_1} {answer_3} {nearest_num}")
#     print(min(answer))
#
#
# if __name__ == "__main__":
#     main()
import sys

input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)