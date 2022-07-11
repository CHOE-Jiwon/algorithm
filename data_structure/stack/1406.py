# 작성일: 2022-07-12
# 문제 링크: https://www.acmicpc.net/problem/1406
##############################################
import sys

class MyClass():

    leftStack = None
    rightStack = None
    inputString = None
    inputList = None
    
    def __init__(self, inputString, inputList):
        self.leftStack = list(inputString)
        self.rightStack = list()
        self.inputString = inputString
        self.inputList = inputList
    
    def L(self):
        if len(self.leftStack) != 0:
            self.rightStack.append(self.leftStack.pop())
    
    def D(self):
        if len(self.rightStack) != 0:
            self.leftStack.append(self.rightStack.pop())
        
    def B(self):
        if len(self.leftStack) != 0:
            self.leftStack.pop()
        
    def P(self, arg):
        self.leftStack.append(arg)

        
    def sol(self):
        for one in self.inputList:
            if one == "D":
                self.D()
            elif one == "L":
                self.L()
            elif one == "B":
                self.B()
            elif one == "P":
                self.P()
            else:
                statement, arg = one.split()
                self.P(arg)

        print(''.join(self.leftStack + self.rightStack[::-1]))

        
if __name__ == "__main__":

    inputString = sys.stdin.readline().strip()

    InputCnt = int(sys.stdin.readline())

    inputList = [sys.stdin.readline().strip() for i in range(InputCnt)]
    
    myClass = MyClass(inputString, inputList)
    result = myClass.sol()