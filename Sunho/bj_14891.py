# 톱니바퀴
# n극 : 0, s극 :1
# 뎈큐 써야할 것 같음
from collections import deque
    
# 이 함수가 deque의 핵심
def turn(arr,dir):
    # 시계방향인 경우
    if dir == 1:
        arr.appendleft(arr.pop())
    # 반시계방향인경우
    if dir == -1:
        arr.append(arr.popleft())

# deque로 정의해주기!!
# 여기서 0 deque에서 빼먹지 않으려면 split이 아닌 strip으로 해줘야함
matrix = [deque(list(map(int,input().strip()))) for _ in range(4)]
k = int(input())    # 회전 횟수
for _ in range(k):
    n, d = map(int, input().split())    # 톱니 번호, 방향(1: 시계, -1: 반시계)\

    rotation = [0, 0, 0, 0]    # 각 회전 턴 별 회전방향 저장
    rotation[n-1] = d

    # 현재 톱니 기준 왼쪽 애들 회전 조정
    for i in range(n-1, 0, -1):
        if matrix[i][6] != matrix[i-1][2]:  # 맞물리는 톱니 다르면
            rotation[i-1] = -rotation[i]    # 반대방향 회전 넣어주기
        else:       
            break   # 같으면 더이상 돌 필요 없음


    # 현재 톱니  기준 오른쪽 애들 회전 조정
    for i in range(n-1, 3):
        if matrix[i][2] != matrix[i+1][6]:
            rotation[i+1] = - rotation[i]
        else:
            break

    for i in range(4):
        turn(matrix[i], rotation[i])

ans = matrix[0][0] + 2 * matrix[1][0] + 4 * matrix[2][0] + 8 * matrix[3][0]
print(ans)
