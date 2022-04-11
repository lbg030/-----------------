n = int(input())
li = list(map(int, input().split()))
li2 = li[:]
count_list = []
idx = 0


for _ in range(n-1):
    value = li[idx]
    temp = idx
    count_list.append(li2.index(value) + 1)
    print(f"value = {value}")
    idx += value
    del li[temp]
    while idx >= len(li):
        print(";;")
        idx -= len(li)

count_list.append(*li)
print(*count_list)
