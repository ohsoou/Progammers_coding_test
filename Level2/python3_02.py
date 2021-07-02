# 기능개발 

import math
def solution(progresses, speeds):
    days = []
    answer = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    
    prev = 0
    j = 0
    answer.append(1)
    
    for i in range(1, len(days)):
        if days[prev] >= days[i] :
            answer[j] += 1
        else:
            answer.append(1)
            prev = i
            j+=1
    
    return answer
