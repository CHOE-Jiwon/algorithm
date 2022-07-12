# 작성일: 2022-07-12
# 문제 링크: https://www.acmicpc.net/problem/1158
# 1 try: 시간초과
##############################################
import sys
from collections import deque

class MyClass():

    queue = None
    result = None

    def __init__(self, N):
        self.queue = deque()
        self.result = list()

        for i in range(N):
            self.queue.append(str(i+1))
    
    def sol(self, K):
        while len(self.queue):
            for i in range(K):
                if i != K - 1:
                    self.queue.append(self.queue.popleft())
                else:
                    self.result.append(self.queue.popleft())
        
        print("<{}>".format(", ".join(self.result)))

if __name__ == "__main__":

    N, K = map(int, sys.stdin.readline().strip().split())

    myClass = MyClass(N)
    result = myClass.sol(K)