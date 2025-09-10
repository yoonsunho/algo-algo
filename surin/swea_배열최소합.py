# 배열 최소 합
# 한 줄에 하나씩 선택 (가로, 세로 모두 다른 칸)

T = int(input())


def dfs(ci, cj, total):
    '''
    ci : 현재 행,
    cj : 현재 열
    '''
    global answer, n

    # 현재의 합이 answer보다 크다면
    if total >= answer:
        return
    
    # 마지막 행까지 갔다면
    if ci == (n - 1):
        if answer > total:
            answer = total
            return
    
    total += matrix[ci][cj]

    for i in range(ci+1, n):
        for j in range(cj+1, n):
            dfs(i, j, total)
    


for tc in range(1, T+1):
    answer = 150

    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append([int(num) for num in input().split()])

    dfs(0, 0, 0)

    print(f"#{tc} {answer}")