import sys
sys.stdin = open('input/input (1).txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 덤프 횟수
    box_list = list(map(int, input().split()))
    answer = 0
    while N > 0:
        max_num = 0
        min_num = 1001
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if box_list[i] >= max_num:
                max_num = box_list[i]
                max_idx = i
            if box_list[i] <= min_num:
                min_num = box_list[i]
                min_idx = i
        if max_num == min_num:
            answer = 0
            break
        box_list[max_idx] -= 1
        box_list[min_idx] += 1
        N -= 1
    answer = max(box_list) - min(box_list)
    print(f'#{tc}', answer)



