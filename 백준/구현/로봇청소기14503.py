"""
    문제에서 서술된 규칙대로 푼다.
    https://resilient-923.tistory.com/164
"""
import copy

def main():
    # 방향 벡터 설정
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    # 입력값 초기화
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    room = []
    for _ in range(n):
        room.append(list(map(int, input().split())))

    # n, m = 11, 10
    # r, c, d = 7, 4, 0
    # room = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    # 알고리즘 서술
    answer = 0
    ny, nx, nd = r, c, d
    cnt = 0
    while True:
        cnt += 1
        # if cnt == 200:
        #     print("start")
        # print(f"{ny} {nx} {nd} {answer}")
        # temp_cnt = 0
        # for row in room:
        #     if temp_cnt == ny:
        #         temp_row = copy.deepcopy(row)
        #         temp_row[nx] = 9
        #         print(temp_row)
        #         temp_cnt += 1
        #         continue
        #     print(row)
        #     temp_cnt += 1
        # print("-----------------")
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if room[ny][nx] == 0:
            room[ny][nx] = 2
            answer += 1

        # 2. 현재 칸의 주변 4칸 중 청소 되지 않은 빈 칸이 없는 경우,
        # 2-1. 주변에 4칸이 존재할 경우. (로봇이 벽면에 붙어 있지 않은 경우)
        if (ny - 1 >= 0) and (ny + 1 < n) and (nx - 1 >= 0) and (nx + 1 < m):
            # 2-1-2. 주변에 4칸 중 청소되지 않은 빈 칸이 없는 경우
            if not ((room[ny-1][nx] == 0) or (room[ny][nx-1] == 0) or
                    (room[ny+1][nx] == 0) or (room[ny][nx+1] == 0)):
                # 2-1-3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                bd = (nd + 2) % 4
                if room[ny+dy[bd]][nx+dx[bd]] != 1:
                    nx += dx[bd]
                    ny += dy[bd]
                    continue
                # 2-1-4. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                else:
                    break
        # 2-2. 주변에 4칸이 없는 경우. (로봇이 벽면에 붙어 있는 경우)
        else:
            if ny == 0:
                if nx == 0:
                    if (nd == 0) or (nd == 1):
                        # 2-1-3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                        bd = (nd + 2) % 4
                        if room[ny + dy[bd]][nx + dx[bd]] != 1:
                            nx += dx[bd]
                            ny += dy[bd]
                            continue
                        # 2-1-4. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                        else:
                            break
                else:  # nx == m-1
                    if (nd == 0) or (nd == 3):
                        # 2-1-3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                        bd = (nd + 2) % 4
                        if room[ny + dy[bd]][nx + dx[bd]] != 1:
                            nx += dx[bd]
                            ny += dy[bd]
                            continue
                        # 2-1-4. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                        else:
                            break
            else:  # ny == n-1
                if nx == 0:
                    if (nd == 1) or (nd == 2):
                        # 2-1-3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                        bd = (nd + 2) % 4
                        if room[ny + dy[bd]][nx + dx[bd]] != 1:
                            nx += dx[bd]
                            ny += dy[bd]
                            continue
                        # 2-1-4. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                        else:
                            break
                else:  # nx == m-1
                    if (nd == 2) or (nd == 3):
                        # 2-1-3. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                        bd = (nd + 2) % 4
                        if room[ny + dy[bd]][nx + dx[bd]] != 1:
                            nx += dx[bd]
                            ny += dy[bd]
                            continue
                        # 2-1-4. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                        else:
                            break

        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        # 3-1. 주변에 4칸이 존재할 경우. (로봇이 벽면에 붙어 있지 않은 경우)
        if (ny - 1 >= 0) and (ny + 1 < n) and (nx - 1 >= 0) and (nx + 1 < m):
            # 3-1-1. 주변에 4칸 중 청소되지 않은 빈 칸이 있는 경우
            if (room[ny - 1][nx] == 0) or (room[ny][nx - 1] == 0) or \
                    (room[ny + 1][nx] == 0) or (room[ny][nx + 1] == 0):
                # 3-1-2. 반시계 방향으로 90도 회전한다.
                nd = (nd + 1) % 4
                # 3-1-3. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                if room[ny+dy[nd]][nx+dx[nd]] == 0:
                    nx += dx[nd]
                    ny += dy[nd]
                # 3-1-4. 1번으로 돌아간다.
                continue
        # 3-2. 주변에 4칸이 없는 경우. (로봇이 벽면에 붙어 있는 경우)
        else:
            if ny == 0:
                if nx == 0:
                    nd += 1
                    if (nd == 2) or (nd == 3):
                        if room[ny+dy[nd]][nx+dx[nd]] == 0:
                            nx += dx[nd]
                            ny += dy[nd]
                        continue
                else:  # nx == m-1
                    nd += 1
                    if (nd == 1) or (nd == 2):
                        if room[ny + dy[nd]][nx + dx[nd]] == 0:
                            nx += dx[nd]
                            ny += dy[nd]
                        continue
            else:  # ny == n-1
                if nx == 0:
                    nd += 1
                    if (nd == 0) or (nd == 3):
                        if room[ny + dy[nd]][nx + dx[nd]] == 0:
                            nx += dx[nd]
                            ny += dy[nd]
                        continue
                else:  # nx == m-1
                    nd += 1
                    if (nd == 0) or (nd == 1):
                        if room[ny + dy[nd]][nx + dx[nd]] == 0:
                            nx += dx[nd]
                            ny += dy[nd]
                        continue

    print(answer)


if __name__ == "__main__":
    main()
