# 이동을 먼저 하고 그 전에 것을 지운다.
# temp 사용 하면 될 꺼 같은데

n = int(input())
li = list(map(int, input().split()))
li2 = li[:]
c_list = [1]
idx = li[0]
value = li[idx]

for _ in range(n-1):
    c_list.append(li2.index(value) + 1)
    print(value)
    idx += value
    value = li[idx]

    while (idx > len(li)):
        idx -= len(li)

    temp = idx
    li.pop(temp)

print(c_list)
