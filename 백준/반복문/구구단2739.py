

def solution(num):
    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")


if __name__ == "__main__":
    num = int(input())
    solution(num)
