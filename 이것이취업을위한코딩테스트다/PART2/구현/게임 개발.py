dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
map_list: list
visited: list


class Status:
    def __init__(self, y, x, d):
        self.x = x
        self.y = y
        self.d = d


def move(status: Status):
    global dx, dy, map_list, visited
    status.d = (status.d + 1) % 4
    nx = status.x + dx[status.d]
    ny = status.y + dy[status.d]

    if is_available(nx, ny):
        status.x = nx
        status.y = ny
        visited[ny][nx] = 1
        return status, True

    return status, False


def is_available(x, y):
    global map_list, visited
    if map_list[y][x] == 1 or visited[y][x] == 1:
        return False
    return True


def main():
    global map_list, visited
    n, m = map(int, input().split())
    a, b, p = map(int, input().split())

    x = (n - 1) - a
    y = (m - 1) - b

    map_list = []
    visited = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(m):
        row = list(map(int, input().split()))
        map_list.append(row)

    success = 0
    status = Status(x, y, p)
    if is_available(x, y):
        visited[y][x] = 1
        success += 1
    else:
        return

    fail = 0
    while fail < 4:
        status, flag = move(status)
        if flag:
            success += 1
            fail = 0
            continue
        else:
            fail += 1

    print(success)


if __name__ == "__main__":
    main()
