# 선택 정렬
def main():
  n = int(input())
  lst = []
  for _ in range(n):
    num = int(input())
    lst.append(num)
  for i in range(len(lst)):
    min_index = i
    for j in range(i+1, len(lst)):
      if lst[min_index] > lst[j]:
        min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
  for i in lst:
    print(i)

if __name__ == "__main__":
  main()
