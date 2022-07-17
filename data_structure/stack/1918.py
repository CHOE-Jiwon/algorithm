# 작성일: 2022-07-16
# 문제 링크: https://www.acmicpc.net/problem/1918
##############################################
import sys
from collections import deque

InputString = deque(sys.stdin.readline().strip())

Q = deque()

isTemp = False

while InputString:
    chr = InputString.popleft()

    Q.append(chr)

    if chr in ["*", "/"]:
        second_operand = InputString.popleft()
        first_operand = Q.popleft()
        operator = Q.popleft()

        Q.append("{}{}{}".format(first_operand, second_operand, operator))

while S:
    
    
    
        