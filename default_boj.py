# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/1874
##############################################
import sys

class MyClass():
    InputString = None
    InputList = None
    
    def __init__(self, InputString, InputList):
        self.InputString = InputString
        self.InputList = InputList
    
    def splitInput(self, one):
        return one.split()
    
    def sol(self):
        

        



if __name__ == "__main__":

    InputString = sys.stdin.readline()

    InputCnt = sys.stdin.readline()

    InputList = [sys.stdin.readline().strip() for i in range(InputCnt)]
    
    myClass = MyClass(InputString, InputList)
    result = myClass.sol()