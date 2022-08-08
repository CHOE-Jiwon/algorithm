# 작성일: 2022-08-07
# 문제 링크: https://www.acmicpc.net/problem/1013
# 1 try: 열심히 풀었는데 틀림!
# 2 try: 사람들은 다 정규식으로 풀었네?
##############################################
import sys
import re

testCaseCnt = int(sys.stdin.readline())

answer = list()

pattern = re.compile('(100+1+|01)+')

for i in range(testCaseCnt):

    InputString = sys.stdin.readline().strip()

    if pattern.fullmatch(InputString):
        answer.append("YES")
    else:
        answer.append("NO")
    
for i in answer:
    print(i)