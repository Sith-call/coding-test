
def main():
    n = list(input())
    n.sort(reverse=True)
    answer = ""
    for i in n:
        answer += i
    print(int(answer))


if __name__ == "__main__":
    main()
