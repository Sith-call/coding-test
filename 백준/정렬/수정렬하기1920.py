

def binary_search(lst: list, target: int):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    n = int(input())
    lst_1 = list(map(int, input().split()))
    m = int(input())
    lst_2 = list(map(int, input().split()))

    lst_1.sort()
    for i in lst_2:
        if binary_search(lst_1, i) != -1:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
