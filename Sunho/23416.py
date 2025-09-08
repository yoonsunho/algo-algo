T = int(input())

for t in range(T):

    N = int(input())

    arr = list(map(int, input().split()))

    min_v = arr[0]
    max_v = arr[0]

    for i in range(1,N):
        if arr[i] > max_v:
            max_v = arr[i]

        elif arr[i] < min_v:
            min_v = arr[i]

    ans = max_v - min_v

    print(f'#{t+1} {ans}')





