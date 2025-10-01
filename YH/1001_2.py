# 프로그래머스 Lv1. 최소직사각형

def solution(sizes):
    answer = 0
    n = len(sizes)
    for i in range(n):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    a, b = 0, 0
    for i in range(n):
        a = max(sizes[i][0], a)
        b = max(sizes[i][1], b)
    answer = a * b
    return answer