# 삽입 정렬
def main():
  n = int(input())
  lst = []
  for _ in range(n):
    num = int(input())
    lst.append(num)
  for i in range(1, len(lst)):
    for j in range(i,0,-1):
      if lst[j] < lst[j-1]:
        lst[j], lst[j-1] = lst[j-1], lst[j]
  for i in lst:
    print(i)
    
 if __name__ == "__main__":
  main()
