# SWEA-1209 SUM

import sys
sys.stdin = open('input/0918.txt', 'r')

for _ in range(10):
    answer = 0
    tc = int(input())
    sum_matrix = [list(map(int, input().split())) for _ in range(100)]
    # 행 합
    for i in range(100):
        answer = max(answer, sum(sum_matrix[i]))
    # 열 합
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += sum_matrix[j][i]
        answer = max(answer, sum_num)
    # 왼쪽 대각선 합
    sum_num = 0
    for i in range(100):
        sum_num += sum_matrix[i][i]
    answer = max(answer, sum_num)
    # 오른쪽 대각선 합
    sum_num = 0
    for i in range(99, -1, -1):
        sum_num += sum_matrix[i][i]
    answer = max(answer, sum_num)

    print(f'#{tc}', answer)