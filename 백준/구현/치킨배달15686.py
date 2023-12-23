"""
    0. 알고리즘이 떠오르지 않는다면 브루트포스로 푼다.
        0-1. 입력값의 크기가 작기 때문에 n^3도 가능하다.
    1. 전체 치킨집 중에서 m개만을 선택한다.
    2. 해당 모든 경우의 수에서 각각 도시의 치킨 거리를 구한다.

"""
from itertools import combinations
def main():
    n, m = map(int, input().split())

    map_list = []
    for _ in range(n):
        map_list.append(list(map(int, input().split())))

    # 1. 전체 치킨집 중에서 m개만을 선택한다.
    chicken_house = []
    for i in range(n):
        for j in range(n):
            if map_list[i][j] == 2:
                chicken_house.append([i, j])

    # 2. 치킨집을 m개 선택한다.
    all_cases = list(combinations(chicken_house, m))
    all_cases = [list(x) for x in all_cases]

    # 3. 모든 경우에서 도시의 치킨집을 구한다.
    all_chicken_distance_of_city = []
    for case in all_cases:
        chicken_distance_of_city = 0
        for i in range(n):
            for j in range(n):
                if map_list[i][j] == 1:
                    chicken_distance_of_house = []
                    for chicken_house in case:
                        chicken_distance_of_house.append((abs(i-chicken_house[0])+abs(j-chicken_house[1])))
                    chicken_distance_of_city += min(chicken_distance_of_house)
        all_chicken_distance_of_city.append(chicken_distance_of_city)

    print(min(all_chicken_distance_of_city))



if __name__ == "__main__":
    main()
