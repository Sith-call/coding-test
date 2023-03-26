
mem: dict
cnt_0: int
cnt_1: int


def fib(n: int):
    global mem
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    elif n in mem.keys():
        return mem[n]
    else:
        a: int = n - 1
        b: int = n - 2
        lst_1 = fib(a)
        lst_2 = fib(b)
        val_1 = lst_1[0] + lst_2[0]
        val_2 = lst_1[1] + lst_2[1]
        mem[n] = [val_1, val_2]
        return mem[n]


def main():
    global mem

    mem = dict()
    mem[0] = [1, 0]
    mem[1] = [0, 1]
    answer = []
    n = int(input())
    for _ in range(n):
        tc = int(input())
        answer.append(fib(tc))

    for i in answer:
        print(f"{i[0]} {i[1]}")


if __name__ == "__main__":
    main()
