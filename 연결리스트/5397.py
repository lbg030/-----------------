n = int(input())


for _ in range(n):
    li = []
    li.extend(list(map(str, input())))
    idx = 0
    ans = []
    # print(li)
    for j in range(len(li)):
        if(li[j] == '<'):
            if(idx > 0):
                idx -= 1
        elif(li[j] == '>'):
            if(idx < len(li) - 1):
                idx += 1

        elif(li[j] == '-'):
            if(li[j] != '>' or li[j] != '<'):
                ans.pop()

        else:
            ans.insert(idx, li[j])
            idx += 1

    print(*ans, sep='')
