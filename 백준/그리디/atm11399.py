

def main():
    p = []
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()

    sum_list = []
    for i in range(len(p)):
        sum_list.append(sum(p[0:i+1]))

    print(sum(sum_list))


if __name__ == "__main__":
    main()
