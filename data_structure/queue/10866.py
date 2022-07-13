# 작성일: 2022-07-13
# 문제 링크: https://www.acmicpc.net/problem/10866
##############################################
import sys
from collections import deque

class MyClass():
    dequeue = None
    
    def __init__(self):
        self.dequeue = deque()
    
    def push_front(self, x):
        self.dequeue.appendleft(x)
    
    def push_back(self, x):
        self.dequeue.append(x)
    
    def pop_front(self):
        if len(self.dequeue) != 0:
            print(self.dequeue.popleft())
        else:
            print(-1)
    
    def pop_back(self):
        if len(self.dequeue) != 0:
            print(self.dequeue.pop())
        else:
            print(-1)
    
    def size(self):
        print(len(self.dequeue))
    
    def empty(self):
        if len(self.dequeue) == 0:
            print(1)
        else:
            print(0)
    
    def front(self):
        if len(self.dequeue) != 0:
            print(self.dequeue[0])
        else:
            print(-1)
    
    def back(self):
        if len(self.dequeue) != 0:
            print(self.dequeue[-1])
        else:
            print(-1)


if __name__ == "__main__":

    InputCnt = int(sys.stdin.readline())

    InputList = [sys.stdin.readline().strip() for i in range(InputCnt)]
    
    myClass = MyClass()

    for input_statement in InputList:
        if ' ' in input_statement:
            statement, arg = input_statement.split()
            getattr(myClass, statement)(arg)
        else:
            getattr(myClass, input_statement)()