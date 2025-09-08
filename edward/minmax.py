T = int(input())

def max_minus_min(arr_):
    max, min = 0, 100000000000000000
    for e in arr_:
        if e > max:
            max = e
        if e < min:
            min = e
    return max - min

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{tc} {max_minus_min(arr)}")
