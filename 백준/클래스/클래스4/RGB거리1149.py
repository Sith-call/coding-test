"""
    greedy로 푸니까 풀리지 않았다.
    매번 최소를 선택하는 경우에는 반례가 존재한다.
    그렇다고 해서 모든 경우의 수를 중복 없이 몇 가지로 나눠서 비교해보는 것도
    지금 당장 생각나진 않는다.
    이후에 dp를 익힌 후에 다시 풀어보겠다.

"""

def main():
    answer = 0
    prev_color = ""
    n = int(input())
    for _ in range(n):
        r, g, b = map(int, input().split())
        lst = [[r, "r"], [g, "g"], [b, "b"]]
        lst.sort()
        for item in lst:
            # if item[1] == prev_color:
            #     continue
            answer += item[0]
            prev_color = item[1]
            print(f"catch {item[1]} {item[0]}")
            break

    print(answer)


if __name__ == "__main__":
    main()
