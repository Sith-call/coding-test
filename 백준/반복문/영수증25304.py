

if __name__ == "__main__":
    expected = int(input())
    n = int(input())
    actual = 0
    for _ in range(n):
        price, cnt = map(int, input().split())
        actual += (price * cnt)
    if expected == actual:
        print("Yes")
    else:
        print("No")
