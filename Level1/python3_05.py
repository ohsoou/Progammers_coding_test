#키패드 누르기 
def solution(numbers, hand):
    answer = ''
    dic = {'L':10, 'R':12}
    if(hand == "left"):
        hand = 'L'
    else:
        hand = 'R'

    for n in numbers:
        if(n in [1,4,7]):
            answer += 'L'
            dic['L'] = n
        elif (n in [3,6,9]):
            answer += 'R'
            dic['R'] = n
        elif (n in [2,5,8,0]):
            if(n == 0):
                n = 11
            right_distance = abs(n-dic['R'])//3+abs(n-dic['R'])%3
            left_distance = abs(n-dic['L'])//3+abs(n-dic['L'])%3

            if(right_distance == left_distance):
                answer += hand
                dic[hand] = n
            elif(right_distance < left_distance):
                answer += 'R'
                dic['R'] = n
            else:
                answer += 'L'
                dic['L'] = n

    return answer
