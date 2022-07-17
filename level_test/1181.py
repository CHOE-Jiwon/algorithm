# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/1181
##############################################
import sys


InputCnt = int(sys.stdin.readline())

InputList = list(set([sys.stdin.readline().strip() for i in range(InputCnt)]))

sorted_list = sorted(InputList, key=lambda x:(len(x), x))

for word in sorted_list:
    print(word)