# 작성일: 2022-07-13
# 문제 링크: https://www.acmicpc.net/problem/17413
##############################################
import sys
from collections import deque

class MyClass():

    word_queue = None
    
    def __init__(self):
        self.word_queue = deque()

    def split_tag(self, InputString):
        splited_list = []

        tmp_str = ''

        for chr in InputString:

            if tmp_str != '' and chr == "<":
                splited_list.append(tmp_str)
                tmp_str = ''

            if chr == ">":
                splited_list.append(tmp_str+">")
                tmp_str = ''
                continue

            tmp_str += chr

        if tmp_str != "": splited_list.append(tmp_str)

        result = ""
        for splited in splited_list:
            if "<" in splited:
                result += splited
            else:
                result += ' '.join([x[::-1] for x in splited.split()])

        print(result)
        

if __name__ == "__main__":

    # InputString = sys.stdin.readline().strip()
    InputString = "<int><max>2147483647<long long><max>9223372036854775807"

    myClass = MyClass()
    result = myClass.split_tag(InputString)