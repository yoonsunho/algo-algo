import sys
sys.stdin = open('input/input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    answer = 0
    N = int(input())
    num_list = input()
    prev_num = False
    sequence = 0
    if num_list[0] == '1':
        prev_num = True
        answer += 1
        sequence = 1
    for i in range(1, N):
        if prev_num != True and num_list[i] == '1':
            sequence += 1
            prev_num = True
            if sequence >= answer:
                answer = sequence
        elif prev_num and num_list[i] == '1':
            sequence += 1
            if sequence >= answer:
                answer = sequence
        else:
            prev_num = False
            sequence = 0

    print(f'#{tc}', answer)