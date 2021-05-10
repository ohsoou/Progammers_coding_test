## 체육복 
def solution(n, lost, reserve):
    answer = 0
    
    for i in lost[:]:
        if(i in reserve):
            lost.remove(i)
            reserve.remove(i)
    for i in lost[:]:
        if(i+1 in reserve):
            lost.remove(i)
            reserve.remove(i+1)
        elif(i-1 in reserve):
            lost.remove(i)
            reserve.remove(i-1)
    answer = n - len(lost)
    return answer
