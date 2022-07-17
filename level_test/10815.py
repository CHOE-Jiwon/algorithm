# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/10815
##############################################
import sys
from collections import Counter


InputCnt = int(sys.stdin.readline())
SList = sys.stdin.readline().split()

InputCnt = int(sys.stdin.readline())
CList = sys.stdin.readline().split()

SCount = Counter(SList)
RList = list()

for C in CList:
    count = SCount[C]
    RList.append(1 if count else 0)

print(*RList)
