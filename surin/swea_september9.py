# 두자리 정수 N
# 9가 있는지 없는지?

def find_9(number: int):
    if "9" in str(number):
        return "Yes"
    else:
        return "No"
    

tc = int(input())

for i in range(1, tc+1):
    target_number = int(input())
    answer = find_9(target_number)
    print(f"#{i} {answer}")