from sys import stdin

n = int(input())
dic = {}
cnt = 0
for _ in range(n):
    name, work = stdin.readline().rstrip().split()

    if work == '-':
        if name not in dic or dic[name] == 0:
            cnt += 1
        elif name in dic:
            dic[name] -= 1

    #work = +
    else:
        if name not in dic:
            dic[name] = 1
        else:
            dic[name] += 1

if len(dic) == 0:
    print(cnt)
else:
    print(sum(dic.values()) + cnt)