

def solution(h, m):
    minutes = (h*60) + m

    minutes -= 45

    nh, nm = 0, 0
    if minutes >= 0:
        nh = minutes // 60
        nm = minutes % 60
    else:
        new_minutes = (24*60) + minutes
        nh = new_minutes // 60
        nm = new_minutes % 60

    print(f"{nh} {nm}")


if __name__ == "__main__":
    h, m = map(int, input().split(" "))
    solution(h, m)
