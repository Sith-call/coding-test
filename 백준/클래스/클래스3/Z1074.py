# """
#     dp로 풀려고 하니, 메모리 초과가 났다.
#     애초에 n에 대한 해답 자체가 용량이 크기 때문이다.
#     https://ggasoon2.tistory.com/11
#     몰라서 답 올림
# """
#
#
# mem: dict
#
# def make_mem(n):
#     global mem
#     new_mem = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
#     if n in mem.keys():
#         return mem[n]
#     else:
#         prev_mem = make_mem(n-1)
#         value = 2**(2*n-2)
#         for i in range(2**n):
#             for j in range(2**n):
#                 if (0 <= i < 2**(n-1)) and (0 <= j < 2**(n-1)):
#                     new_mem[i][j] = prev_mem[i][j]
#                 elif (0 <= i < 2**(n-1)) and (2**(n-1) <= j < 2**n):
#                     new_mem[i][j] = prev_mem[i][j-(2**(n-1))] + value
#                 elif (2**(n-1) <= i < 2**n) and (0 <= j < 2**(n-1)):
#                     new_mem[i][j] = prev_mem[i-(2**(n-1))][j] + (value * 2)
#                 elif (2**(n-1) <= i < 2**n) and (2**(n-1) <= j < 2**n):
#                     new_mem[i][j] = prev_mem[i - (2 ** (n - 1))][j - (2**(n-1))] + (value * 3)
#     mem[n] = new_mem
#     return mem[n]
#
#
# def main():
#     global mem
#
#     mem = dict()
#
#     mem[1] = [[1, 2],
#               [3, 4]]
#
#     mem[2] = [[1, 2, 5, 6],
#               [3, 4, 7, 8],
#               [9, 10, 13, 14],
#               [11, 12, 15, 16]]
#
#     n, r, c = map(int, input().split())
#
#     make_mem(n)
#
#     print(mem[n][r][c]-1)
#
#
# if __name__ == "__main__":
#     main()

while N != 0:

    N -= 1

    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)

    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    # 4사분면
    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(ans)