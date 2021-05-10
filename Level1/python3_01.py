"""
n개의 배열에서 n/2개로 만들 수 있는 조합 중 원소가 가장 다양할 때 원소의 개수 
"""

def solution(nums):
    unique_list = set(nums)
    select_len = len(nums)/2
    max_len = len(unique_list)
    return max_len if max_len <= select_len else select_len
