

def main():
    n = int(input())
    lst = []
    answer = []
    for _ in range(n):
        val = input()
        data = [len(val), val]
        lst.append(data)
    lst.sort()
    temp_str = ""
    for k, i in lst:
        if i == 0:
            answer.append(i)
            temp_str = i
        if i == temp_str:
            continue
        else:
            temp_str = i
            answer.append(i)
    for j in answer:
        print(j)


if __name__ == "__main__":
    main()
