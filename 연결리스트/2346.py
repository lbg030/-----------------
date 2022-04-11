n = int(input())
li = list(map(int, input().split()))
li2 = li[:]

count_list = []

idx = 0
for _ in range(n):
    a = li[idx]
    del li[idx]
    idx += a

    count_list.append(li2.index(a) + 1)
    print(f"a = {a}, li2.index(a) = {li2.index(a)}")

    if(idx > len(li)):
        idx -= len(li)


print(*count_list)

# 1 4 5 3 2
