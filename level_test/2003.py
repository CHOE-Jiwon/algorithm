# 작성일: 2022-07-18
# 문제 링크: https://www.acmicpc.net/problem/2003 
# 1 try: 시간 초과 -> O(n^2)인데... 왜...? -> 다시 보니 합을 넘었을 때 브레이크가 없음.
# 2 try: 그래도 시간초과
# 투 포인터 개념
# https://www.youtube.com/watch?v=ttLRltNDiCo&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=40
##############################################
import sys
import time

num_cnt, target_sum = map(int,sys.stdin.readline().split())

InputList = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
partial_sum = InputList[end]
result_cnt = 0

for start in range(num_cnt):

    while partial_sum < target_sum and end < num_cnt - 1:
        end += 1
        partial_sum += InputList[end]

    if partial_sum == target_sum:
        result_cnt += 1
        partial_sum -= InputList[start]
    elif partial_sum > target_sum:
        partial_sum -= InputList[start]
    

print(result_cnt)
