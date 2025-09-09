import sys
sys.stdin = open('input/in.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  #가로 길이
    box_list = list(map(int, input().split()))
    answer = 0
    for i in range(0, N-1):
        for_answer = 0
        for j in range(i+1, N):
            if box_list[i] > box_list[j]:
                for_answer += 1
        if for_answer >= answer:
            answer = for_answer
    print(f'#{tc}', answer)
