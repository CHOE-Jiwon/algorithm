##############################################
# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/9012
##############################################
import sys

class MyClass():
    vps = None
    vps_stack = None

    def __init__(self, vps):
        self.vps = vps
        self.vps_stack = list()

    def validate(self):
        isValid = True

        if self.vps.count("(") == self.vps.count(")"):

            for char in self.vps:
                if char == "(":
                    self.vps_stack.append(1)
                else:
                    if len(self.vps_stack) == 0:
                        isValid = False
                        break
                    else:
                        self.vps_stack.pop()
        else:
            isValid = False
        
        return "YES" if isValid else "NO"

if __name__ == "__main__":

    input_cnt = int(sys.stdin.readline())

    input_list = [sys.stdin.readline().strip() for i in range(input_cnt)]
    
    for vps in input_list:
        myClass = MyClass(vps)
        print(myClass.validate())
