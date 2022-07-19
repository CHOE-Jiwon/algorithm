# 작성일: 2022-07-18
# 문제 링크: https://www.acmicpc.net/problem/1912
##############################################
import sys

InputCnt = int(sys.stdin.readline())

InputList = map(int, sys.stdin.readline().split())

max_sum = -1001
sum = 0

for integer in InputList:
    sum += integer

    if max_sum < sum:
        max_sum = sum
    
    if sum < 0:
        sum = 0

print(max_sum)