# 최소 배열합

import sys
sys.stdin = open('input/sample_input1.txt', 'r')

def dfs(row, sum_num):
    global answer

    if row == N:
        answer = min(answer, sum_num)
        return

    if sum_num > answer:
        return

    for column in range(N):
        if visited[column] == 0:
            visited[column] = 1
            dfs(row + 1, sum_num + matrix[row][column])
            visited[column] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 10000
    visited = [0] * N
    dfs(0, 0)

    print(f'#{tc}', answer)