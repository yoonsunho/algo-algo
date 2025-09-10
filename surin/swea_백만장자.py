# 1859
# 1. 연속된 N일 동안의 물건의 매매가를 예측해서 알고 있음.
# 2. 당국의 감시망에 걸리지 않도록 하루 최대 1만큼 구입 가능
# 3. 판매는 얼마든지 가능

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 최대 이익
    answer = 0
    # 자연수
    N = int(input())
    # 매매가
    money_list = [int(n) for n in input().split()]

    # 현재 시점의 매매가
    current_money = money_list[-1]
    # 거꾸로 돌아간다. (현재 -> 과거
    for money in money_list[::-1]:
        if current_money >= money:
            answer += (current_money - money)
        else:
            current_money = money

    print(f"#{tc} {answer}")