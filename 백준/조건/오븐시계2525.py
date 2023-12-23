
def solution(h, m, c):
    minutes = (h * 60) + m

    minutes += c

    nh, nm = 0, 0
    if minutes < 1440:
        nh = minutes // 60
        nm = minutes % 60
    else:
        new_minutes = minutes - (24 * 60)
        nh = new_minutes // 60
        nm = new_minutes % 60

    print(f"{nh} {nm}")


if __name__ == "__main__":
    h, m = map(int, input().split(" "))
    c = int(input())
    solution(h, m, c)
