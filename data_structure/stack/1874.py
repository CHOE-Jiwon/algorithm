##############################################
# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/1874
# 1 try: 시간 초과
##############################################
import sys

class MyClass():
    
    check_point = None
    stack = None

    def __init__(self):
        self.check_point = 0
        self.stack = list()

    def IsExist(self, n):
        return n in self.stack
    
    def push(self):
        self.check_point += 1
        self.stack.append(self.check_point)
        print("+")

    def pop(self):
        self.stack.pop()
        print("-")
    
    def sol(self, input_list):

        for input_num in input_list:
            
            if input_num > self.check_point:
                for i in range(self.check_point, input_num):
                    self.push()
            elif input_num == self.check_point:
                self.push()
                self.pop()
            else:
                if self.IsExist(input_num):
                    self.pop()
                else:
                    print("NO")

if __name__ == "__main__":

    input_cnt = int(sys.stdin.readline())

    input_list = [int(sys.stdin.readline().strip()) for i in range(input_cnt)]
    
    myClass = MyClass()
    myClass.sol(input_list)