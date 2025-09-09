# 1204
# 최빈수 : 특정 자료에서 가장 여러 번 나타나는 값
# 학생 수 : 1000
# 각 학생의 점수 0 ~ 100

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    tc = int(input())
    
    answer = 0
    counting_list = [0] * 101
    
    scores = input()
    scores = [int(score) for score in scores.split()]

    for score in scores:
        counting_list[score] += 1

    many_number = max(counting_list)
    for i, students in enumerate(counting_list[::-1]):
        if students == many_number:
            break
    
    answer = 100 - i

    print(f"#{tc} {answer}")


