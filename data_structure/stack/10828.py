##############################################
# 작성일: 2022-07-05
# 문제 링크: https://www.acmicpc.net/problem/10828
# 1 try: 시간초과
# 2 try: 정답
#   - statement split 코드에 있던 try except 지우고, if else로 바꿈.
#   - MyStack 클래스의 push 함수를 제외한 나머지 함수에서 받는 인자값을 지움.
#   - split 을 한 번만 씀... 이게 주요한 원인인것 같음.
##############################################

import time

class MyStack():

    def __init__(self):
        self.stack = list()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.empty() == 0 else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if len(self.stack)==0 else 0

    def top(self):
        return self.stack[-1] if self.empty() == 0 else -1

if __name__ == "__main__":
    input_cnt = int(input().strip())

    loop_cnt = 0
    statement_list = list()

    while(loop_cnt < input_cnt):
        statement_list.append(input().strip())
        loop_cnt += 1

    start_time = time.time()
    myStack = MyStack()

    result = None
    for statement in statement_list:
        splited_statement = statement.split()

        if len(splited_statement) > 1:
            func_name, arg = splited_statement
            result = getattr(myStack, func_name)(arg)
        else:
            func_name = splited_statement[0]
            result = getattr(myStack, func_name)()

    
        if result is not None:
            print(result)
    
    end_time = time.time()
    print(end_time-start_time)