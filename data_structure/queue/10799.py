# 작성일: 2022-07-13
# 문제 링크: https://www.acmicpc.net/problem/10799
##############################################
import sys

class MyClass():
    cnt = None
    pipe = None
    
    def __init__(self):
        self.cnt = 0
        self.pipe = 0
    
    def sol(self, InputString):

        for idx in range(0, len(InputString)-1):
            if InputString[idx] == "(" and InputString[idx+1] == "(":
                self.pipe += 1
            elif InputString[idx] == "(" and InputString[idx+1] == ")":
                self.cnt += self.pipe
            elif InputString[idx] == ")" and InputString[idx+1] == ")":
                self.pipe -= 1
                self.cnt += 1
            elif InputString[idx] == ")" and InputString[idx+1] == "(":
                pass
        
        print(self.cnt)


if __name__ == "__main__":

    InputString = sys.stdin.readline()
    
    myClass = MyClass()
    result = myClass.sol(InputString)