#내적 

def solution(a, b):
    sum=0
    for i in range(len(a)):
        sum+=a[i]*b[i]

    answer = sum
    return answer
