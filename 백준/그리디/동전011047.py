

def main():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    coins.reverse()

    count = 0
    for i in coins:
        if i <= k:
            count += k // i
            k = k % i

    print(count)


if __name__ == "__main__":
    main()
