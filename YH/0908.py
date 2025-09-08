import sys
sys.stdin = open('input\sample_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    answer = 0
    buildings = list(map(int, input().split()))
    buildings_len = len(buildings)  # 가로 길이
    for i in range(2, buildings_len-1):
        right_top = 0
        left_top = 0
        top = 0
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            if buildings[i-1] >= buildings[i-2]:
                left_top = buildings[i-1]
            else:
                left_top = buildings[i-2]
            if left_top >= top:
                top = left_top
            if buildings[i+1] >= buildings[i+2]:
                right_top = buildings[i+1]
            else:
                right_top = buildings[i+2]
            if right_top >= top:
                top = right_top
            answer += buildings[i] - top

    print(f'#{tc}', answer)