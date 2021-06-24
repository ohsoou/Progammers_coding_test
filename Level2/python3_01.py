# 전화번호 목록

def solution(phone_book):
    answer = True

    phone_nums = sorted(phone_book)

    for i in range(1, len(phone_nums)):
        prev_num = phone_nums[i-1]
        current_num = phone_nums[i]
        if(current_num.startswith(prev_num)):
            return False

    return answer