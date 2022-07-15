# 작성일: 2022-07-15
# 문제 링크: https://www.acmicpc.net/problem/17298
# 1 try: 시간초과
# 2 try: 틀렸음 (똑같은 수가 들어올 수도 있다...)
# 3 try: 시간초과
# 4 try: 유튜브보고 정답보고 이해하는데 오래걸렸음 -> 근데 시간초과???
# 5 try: 클래스 생성 버리고 푸니까 통과...
##############################################
import sys
from collections import deque

if __name__ == "__main__":

    InputCnt = int(sys.stdin.readline())

    A = list(map(int, sys.stdin.readline().strip().split()))
    S = deque()
    R = [-1]*InputCnt
    
    for i in range(InputCnt):
        while S and (A[i] > A[S[-1]]):
            R[S.pop()] = A[i]

        S.append(i)

    print(*R)