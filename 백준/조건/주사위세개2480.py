from collections import Counter


def solution(lst):
    dct = Counter(lst)
    max_cnt = 0
    max_key = 0
    price = 0
    for key in dct.keys():
        if dct[key] > max_cnt:
            max_cnt = dct[key]
            max_key = key

    if max_cnt == 3:
        price = 10000 + max_key * 1000
    elif max_cnt == 2:
        price = 1000 + max_key * 100
    else:
        price = max(lst) * 100

    print(price)


if __name__ == "__main__":
    lst = list(map(int, input().split(" ")))
    solution(lst)
