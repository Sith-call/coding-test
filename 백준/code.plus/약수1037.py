
def is_real(n, a):
    if n % a == 0 and a != 1 and a != n:
        return True
    else:
        return False


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    a = nums[0]
    b = nums[len(nums) - 1]
    print(a*b)


if __name__ == "__main__":
    main()
