# 백준 14501 퇴사

# N = int(input()) # 퇴사까지 남은 일
# counselling = []
# for _ in range(N):
#     Ti, Pi = map(int, input().split())
#     counselling.append([Ti, Pi])
# max_answer = 0
#
# for i in range(N):
#     answer = 0
#     if i + counselling[i][0] > N:
#         break
#     answer += counselling[i][1]
#     j = i + counselling[i][0]
#     while j < N:
#         for k in range(j, N):
#             if k + counselling[k][0] > N:
#                 break
#             answer += counselling[k]
#         j +=
#
#
#     max_answer = max(max_answer, answer)
# print(max_answer)
N = int(input())
T = [0] * (N + 2)
P = [0] * (N + 2)
for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

dp = [0] * (N + 2)

for i in range(N, 0, -1):
    end_day = i + T[i]
    if end_day <= N + 1:  # 상담이 끝나는 날이 퇴사 전이면
        dp[i] = max(dp[i+1], P[i] + dp[end_day])
    else:  # 상담 못 하는 경우
        dp[i] = dp[i+1]

print(dp[1])