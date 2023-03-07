n: int
def verify(nx, ny, dx, dy):
    x = nx + dx
    y = ny + dy
    if x < 1 or x > n or y < 1 or y > n:
        return False
    return True


def main():
    global n
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = int(input())

    nx = 1
    ny = 1

    infos = map(str, input().split())

    for info in infos:
        if info == "L":
            i = 0
            if verify(nx, ny, dx[i], dy[i]):
                nx += dx[i]
                ny += dy[i]
        elif info == "R":
            i = 1
            if verify(nx, ny, dx[i], dy[i]):
                nx += dx[i]
                ny += dy[i]
        elif info == "U":
            i = 2
            if verify(nx, ny, dx[i], dy[i]):
                nx += dx[i]
                ny += dy[i]
        elif info == "D":
            i = 3
            if verify(nx, ny, dx[i], dy[i]):
                nx += dx[i]
                ny += dy[i]

    print(f"{ny} {nx}")


if __name__ == "__main__":
    main()
