
def solution(num: int) -> int:
    count = 0
    temp = 1
    while True:
        count += 1
        if temp % num == 0:
            return count
        temp = (temp % num) * 10 + 1


def main():
    while True:
        try:
            n = int(input())
        except:
            break

        print(solution(n))


if __name__ == "__main__":
    main()
