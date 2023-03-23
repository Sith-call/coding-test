
chess: list
n: int
count: int = 0
queens: list  # [[x1,y1], [x2,y2]]


def backtracking(y, x):
    global chess, n, count, queens
    if chess[y][x] == 1 and not check_queen_available(y, x):
        return
    check_queen_range(y, x, chess)
    queens.append([y, x])
    count += 1
    for i in range(1, n+1):  # y
        for j in range(1, n+1):  # x
            if :


                backtracking(i, j)
                uncheck_queen_range(i, j, chess)
                queens.pop()


def check_queen_range(y, x, chess):
    global n
    # 수직선
    for i in range(1, n+1):
        chess[y][i] = 1
        chess[i][x] = 1
    # 기울기가 1인 대각선
    for nx in range(1, n+1):
        ny = (nx - x) + y
        if ny < 1 or ny > n:
            continue
        chess[ny][nx] = 1
    # 기울기가 -1인 대각선
    for nx in range(1, n + 1):
        ny = (-1)*(nx - x) + y
        if ny < 1 or ny > n:
            continue
        chess[ny][nx] = 1


def uncheck_queen_range(y, x, chess):
    global n
    # 수직선
    for i in range(1, n+1):
        chess[y][i] = 0
        chess[i][x] = 0
    # 기울기가 1인 대각선
    for nx in range(1, n+1):
        ny = (nx - x) + y
        if ny < 1 or ny > n:
            continue
        chess[ny][nx] = 0
    # 기울기가 -1인 대각선
    for nx in range(1, n + 1):
        ny = (-1)*(nx - x) + y
        if ny < 1 or ny > n:
            continue
        chess[ny][nx] = 0


def check_queen_available(y, x):
    global n, queens
    chess = [[0 for _ in range(n+1)] for _ in range(n+1)]
    check_queen_range(y, x, chess)
    for queen in queens:
        x = queen[0]
        y = queen[1]
        if chess[y][x] == 0:
            continue
        return False
    return True


def main():
    global chess, n, count, queens
    n = int(input())
    chess = [[0 for _ in range(n+1)] for _ in range(n+1)]
    queens = []

    for i in range(1, n+1):  # y
        for j in range(1, n+1):  # x
            backtracking(i, j)

    print(count)


if __name__ == "__main__":
    main()

# 퀸을 놓는다
# 퀸의 영역을 표시한다
# 다음 퀸을 놓을 때 제약 조건
#   1. 퀸의 영역이 아닌 곳에 놓는다.
#   2. 놓여질 퀸이 다른 퀸을 잡아선 안된다.