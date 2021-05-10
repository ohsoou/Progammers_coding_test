"""
참여자들 중 완주하지 못한 단 한명을 찾아내기 
"""

def solution(participant, completion):
    answer = ''
    dic = {}
    
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            
    for i in completion:
        if (i in dic):
            if dic[i] == 1 :
                del dic[i]
            else:
                dic[i]-= 1
                
    for key, value in dic.items():
        if(value == 1):
            answer = key
    return answer
