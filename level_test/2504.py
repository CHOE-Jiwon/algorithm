# 작성일: 2022-07-24
# 문제 링크: https://www.acmicpc.net/problem/2504
# 1 try: 정규표현식 사용. 시간초과
# 2 try: RuntimeError(TypeError)
# 도저히 모르겠어서 정답 봤습니다. 아직도 이해가 잘 안가네요.
##############################################
import sys
from collections import deque

InputString = deque(sys.stdin.readline().strip())
stack = deque()

tmp = 1
result = 0

# while InputString:
for i in range(len(InputString)):
    cur = InputString[i]

    if cur == "(":
        stack.append(cur)
        tmp *= 2
    elif cur == "[":
        stack.append(cur)
        tmp *= 3
    elif cur == ")":
        # 짝이 없거나, 짝이 안맞는 경우
        if not stack or stack[-1] == "[":
            result = 0
            break
        if InputString[i-1] == "(": 
            result += tmp
        stack.pop()
        tmp /= 2
    elif cur == "]":
        # 짝이 없거나, 짝이 안맞는 경우
        if not stack or stack[-1] == "(":
            result = 0
            break
        if InputString[i-1] == "[":
            result += tmp
        stack.pop()
        tmp /= 3

if stack:
    result = 0    
print(int(result))