"""
    이 문제를 통해 배울 수 있는 점은 주어진 문제의 수학적 이해의 중요성이다.
    알고리즘의 여러 절차를 하나의 수식으로 압축시킬 수 있다.
    예를 들자면 바로 이 문제이다.
    이 문제는 모든 경우의 수를 파악해보는 브루트 포스를 이용하여 풀 수 있다.
    그렇게 된다면 n^2 시간 복잡도를 갖는다.
    왜냐하면 n개의 항이 있을 경우 연속된 k개의 항을 묶어서 계산해야 한다.
    이때 k가 1부터 n까지 순환해야 한다.
    그리고 주어진 k를 이용하여 전체 수식을 순환해야 한다.
    위의 두 가지 순환에 의해서 시간 복잡도는 n^2가 나온다.

    ==> 알고리즘을 하나의 수식으로 압축할 여지가 있는지 생각해본다.

    그러나 이 문제에서 최솟값이란 것에 집중하여 -와 - 사이에 존재하는 항만을 괄호를 친다면,
    알고리즘이 압축될 수 있다.

    1. 모든 연산이 -인 경우
    -> 어디에 괄호를 치든 상관 없다
    2. 모든 연산이 +인 경우
    -> 어디에 괄호를 치든 상관 없다
    3. -와 +가 섞여 있는 경우
    -> -을 기준으로 파싱한 것들 중에 가장 값이 큰 것에 괄호를 친다.

    => 3번을 겨냥한 알고리즘이 1,2번 케이스를 모두 포괄한다.

    https://puleugo.tistory.com/29
"""
import sys
import re
sys = sys.stdin.readline


def main():
    raw_input = input()
    input_str = re.split("([-|+|*])", raw_input)
    raw_formula = ""
    for i in input_str:
        if not (i == "*" or i == "+" or i == "-"):
            raw_formula += str(int(i))
        else:
            raw_formula += i

    formulas = raw_formula.split("-")

    max_idx = 0
    for i in range(len(formulas)):
        if eval(formulas[i]) > eval(formulas[max_idx]):
            max_idx = i

    answer = ""
    for i in range(len(formulas)):
        if i == 0 and i != max_idx:
            answer += formulas[i]
        elif i == max_idx:
            answer += "-(" + formulas[i] + ")"
        else:
            answer += "-" + formulas[i]

    print(eval(answer))


if __name__ == "__main__":
    main()
