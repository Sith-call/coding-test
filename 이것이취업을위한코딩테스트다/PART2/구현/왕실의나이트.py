dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def check(x, y):
    if x < 1 or x > 8 or y < 1 or y > 8:
        return False
    return True


def solution(x, y):
    global dy, dx
    answer = 0

    for i in range(4):

        nx = x + 2 * dx[i]
        ny = y + 2 * dy[i]

        if i % 2 == 0:
            nny_1 = ny + 1
            nny_2 = ny - 1
            if check(nx, nny_1):
                answer += 1
            if check(nx, nny_2):
                answer += 1
        else:
            nnx_1 = nx + 1
            nnx_2 = nx - 1
            if check(nnx_1, ny):
                answer += 1
            if check(nnx_2, ny):
                answer += 1

    return answer


def main():
    pos = input()

    x = ord(pos[0]) - 96
    y = int(pos[1])

    print(solution(x, y))


if __name__ == "__main__":
    main()
