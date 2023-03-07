answer: int = 0


def check():
    global answer
    for minute in range(60):
        for second in range(60):
            if ("3" in str(minute)) or ("3" in str(second)):
                answer += 1


def main():
    global answer
    n = int(input())
    for hour in range(n+1):
        if "3" in str(hour):
            answer += (60 * 60)
            continue
        check()
    print(answer)


if __name__ == "__main__":
    main()
