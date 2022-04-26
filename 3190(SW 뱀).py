# 뱀의 머리는 처음에 오른쪽
# 자기 자신한테 닿거나 벽에 닿으면 사망
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시간
count = 0

size = int(input())
# 보드 판 [ 모두 0으로 초기화 ]
board = [[0] * size for _ in range(size)]


apple = int(input())
# 사과 위치
for _ in range(apple):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

moving = int(input())
for _ in range(moving):
    None
