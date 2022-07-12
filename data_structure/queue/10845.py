# 작성일: 2022-07-12
# 문제 링크: https://www.acmicpc.net/problem/10845
##############################################
import sys

class MyClass():
    
    queue = None
    InputList = None
    
    def __init__(self, InputList):
        self.queue = list()
        self.InputList = InputList
    
    def push(self, arg):
        self.queue.append(arg)
    
    def pop(self):
        print(self.queue.pop(0) if len(self.queue) != 0 else -1)
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        print(1 if len(self.queue) == 0 else 0)
    
    def front(self):
        print(self.queue[0] if len(self.queue) != 0 else -1)
    
    def back(self):
        print(self.queue[-1] if len(self.queue) != 0 else -1)
    
    def sol(self):
        for one in self.InputList:
            if one == "front":
                self.front()
            elif one == "back":
                self.back()
            elif one == "size":
                self.size()
            elif one == "empty":
                self.empty()
            elif one == "pop":
                self.pop()
            else:
                statement, arg = one.split()
                self.push(arg)
        

if __name__ == "__main__":

    InputCnt = int(sys.stdin.readline())

    InputList = [sys.stdin.readline().strip() for i in range(InputCnt)]
    
    myClass = MyClass(InputList)
    result = myClass.sol()