

def solution(num1: int, num2: int) -> None:
    results = []

    nums = list(map(int, list(str(num2))))
    nums.reverse()

    for num in nums:
        data = (num1*num)
        results.append(data)

    final_result = 0
    for idx, result in enumerate(results):
        final_result = final_result + (result * (10**idx))

    results.append(final_result)

    for result in results:
        print(result)


if __name__ == "__main__":

    num1 = int(input())
    num2 = int(input())

    solution(num1, num2)
