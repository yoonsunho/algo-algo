# SWEA-10580 전봇대

import sys
sys.stdin = open('input/0916.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 전선의 개수
    line = []
    answer = 0
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        line.append([Ai, Bi])
    for i in range(N-1):
        for j in range(i+1, N):
            if (line[i][0] > line[j][0]) and (line[i][1] < line[j][1]):
                answer += 1
            if (line[i][0] < line[j][0]) and (line[i][1] > line[j][1]):
                answer += 1

    print(f'#{tc}', answer)