n = int(input())


for _ in range(n):
    li = []
    li.append(list(input()))
    idx = 0
    for j in range(len(li)):
        if(li[j] == '<' and idx > 0):
            idx -= 1
        if(li[j] == '>' and idx < len(li) - 1):
            idx += 1
