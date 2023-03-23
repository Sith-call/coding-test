

def main():
    n, m = map(int, input().split())
    answer = 0
    cards = []

    for _ in range(n):
        card = list(map(int, input().split()))
        cards.append(card[0:m])

    for card in cards:
        value = min(card)
        if value > answer:
            answer = value

    print(answer)


if __name__ == "__main__":
    main()
