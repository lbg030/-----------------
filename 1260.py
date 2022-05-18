# DFS BFS

#BFS popleft 위해서 deque 사용
from collections import deque

n, m, start = map(int, input().split())

#dfs bfs 그래프 따로 따로
graph = [[0] * (n+1) for _ in range(n+1)]
graph2 = [[0] * (n+1) for _ in range(n+1)]

#만약 예제 2번처럼 999 1000 되어 있는 상황에서 1000으로 시작하면 시작을 할 수 조차 없고
#연결되어있는게 1-3 이나 3-1이나 같기 때문에 배열을 생성해 준다.
for _ in range(m):
    n1,n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1
    graph2[n1][n2] = graph2[n2][n1] = 1

#좀 더 쉬움
def dfs(start, answer = []):
    answer.append(start)
    #이 포문을 통해서 0인것은 지나치고 어느것이랑 연결되어있는지 체크
    for i in range(1, n+1):
        if graph[start][i] == 1 and i not in answer:
            #2중 배열을 선언하였기 때문에 이미 지나갔단 의미로 0으로 바꿔 주어야 한다.
            graph[start][i] = graph[i][start] = 0
            # 재귀적으로 사용
            dfs(i, answer)
            #만약 재귀가 다 끝났으면 return
            #만약 연결되어 있지 않은 간선이 있으면 
            #연결이 안된것이기 때문에 무시하고 return 해도 됨.
    return answer

#BFS
def bfs(start):
    ans = deque()
    lst = deque()
    lst.append(start)
    while lst:
        start = lst.popleft()
        ans.append(start)
        for i in range(1, n+1):
            if graph2[start][i] == 1 :
                if i not in lst:
                    lst.append(i)
                graph2[start][i] = graph2[i][start] = 0
        # print(f"ans = {ans}, lst = {lst}")
        # print(lst, ans)
    #lst의 값이 비었으면 ans 출력
    else :
        # ans.popleft()
        # print(lst, ans)
        return ans
    
dfsAnswer = dfs(start)
bfsAnswer = bfs(start)
print(*dfsAnswer)
print(*bfsAnswer)