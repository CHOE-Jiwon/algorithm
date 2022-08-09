# 작성일: 2022-08-09
# 문제 링크: https://www.acmicpc.net/problem/1259
##############################################
import sys

input_str = sys.stdin.readline().strip()

while (input_str != "0"):
    result = "yes"

    for i in range(len(input_str)//2 + 1):
        if input_str[i] != input_str[-(i+1)]:
            result = "no"
    
    print(result)
    
    input_str = sys.stdin.readline().strip()