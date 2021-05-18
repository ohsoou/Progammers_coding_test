#모의고사  

def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    j = 0
    k = 0
    m = 0
    correct = {1: 0, 2: 0, 3: 0}
    for i in answers:
        j = 0 if j == len(p1) else j
        k = 0 if k == len(p2) else k
        m = 0 if m == len(p3) else m
        correct[1] += 1 if p1[j] == i else 0
        correct[2] += 1 if p2[k] == i else 0
        correct[3] += 1 if p3[m] == i else 0
        j += 1
        k += 1
        m += 1

    answer = [k for k,v in correct.items() if max(correct.values()) == v]
    return answer
