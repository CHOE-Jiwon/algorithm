# 작성일: 2022-07-16
# 문제 링크: https://www.acmicpc.net/problem/1935
# 1 try: IndexError
# 2 try: InputList에서 숫자 꺼내오는 부분을 pop이 아니라 index 타서 가져오는 형태로 바꿔줬음.
# -> pop에서는 왜 인덱스 에러가 났을까...
##############################################
import sys
from collections import deque


InputCnt = int(sys.stdin.readline())

Expression = sys.stdin.readline().strip()

InputList = deque([sys.stdin.readline().strip() for i in range(InputCnt)])

stack = deque()


for i in Expression:

    if i not in ["+", "-", "*", "/"]:
        stack.append(InputList[ord(i) - ord('A')])
    else:
        second_operand = stack.pop()
        first_operand = stack.pop()
        
        new_operand = str(eval(first_operand + i + second_operand))

        stack.append(new_operand)

result = float(stack.pop())
print(f"{result:.2f}")
