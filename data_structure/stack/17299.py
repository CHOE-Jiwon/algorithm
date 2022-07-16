# 작성일: 2022-07-16
# 문제 링크: https://www.acmicpc.net/problem/17299
# 1 try: 오큰수랑 동일하게 했는데 시간초과
# 2 try: list.count 를 사용하여 카운트 비교하는거를 Counter 사용하는 것으로 변경.
##############################################
import sys
from collections import deque, Counter

if __name__ == "__main__":

    InputCnt = int(sys.stdin.readline())

    A = list(map(int, sys.stdin.readline().strip().split()))
    C = Counter(A)
    S = deque()여
    R = [-1]*InputCnt
    
    for i in range(InputCnt):
        while S and (C[A[i]] > C[A[S[-1]]]):
            R[S.pop()] = A[i]

        S.append(i)

    print(*R)