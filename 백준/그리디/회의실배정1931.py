"""
    그리디는 결국 높은 순 또는 낮은 순의 정렬 기준을 하나 정하고
    이를 바탕으로 대입을 해봐야 한다.
    그리고 최종적으로 해당 정렬 기준이 옳은지 증명해야 한다.
    이때 정렬 기준이 복잡해질 수 있다.
    문제에서 그리고 정렬 기준에 대한 힌트를 준다. 이를 잘 캐치하자
"""
# import sys
# input = sys.stdin.readline()


def main():
    n = int(input())
    data = []
    for _ in range(n):
        s, e = map(int, input().split())
        d = e - s
        data.append([s, e])

    data.sort(key=lambda x: (x[1], x[0]))

    answer = 1
    end_time = data[0][1]
    for i in range(1, n):
        if data[i][0] >= end_time:
            answer += 1
            end_time = data[i][1]
            # print(f"{datum[1]} {datum[0]}")

    print(answer)
    # print(t)
    # print(data)


if __name__ == "__main__":
    main()
