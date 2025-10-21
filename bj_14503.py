di = [-1,0,1,0]
dj = [0,1,0,-1]

def check(i,j,d):        # 시작좌표, 방향
    x, y = i, j
    count = 0       # 청소할 칸 수 담을 변수
    while True:
        st_i, st_j = -1, -1     # while문 실행될 때 마다 초기화 될 임의 값 담을 변수
        if matrix[x][y] == 0:
            count += 1
            matrix[x][y] += 2
        for k in [(d+3)%4, (d+2)%4, (d+1)%4, d%4]:      # 4방향 90도 왼방향 회전순 탐색
            ni = x + di[k]
            nj = y + dj[k]
            if 0<= ni < N and 0<= nj < M and matrix[ni][nj] == 0:
                st_i, st_j, d = ni, nj, k
                break
        else:       # 2번상황 사방에 청소할 곳 없음 (break문에서 안걸린상황 + if 문에서 안걸린 상황)
            bi = x + di[(d+2) % 4]
            bj = y + dj[(d+2) % 4]
            if 0 <= bi < N and 0 <= bj < M :
                if matrix[bi][bj] == 1:
                    break
                else:
                    st_i, st_j = bi, bj

        x, y = st_i, st_j

    return count

N, M = map(int, input().split())
si, sj, direction = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# print(matrix)


ans = check(si, sj, direction)

print(ans)
