# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/1874
# 틀린 코드임. 왜 틀렸는지 모르겠음.
# for 문 저거 출력해봐라;;;
# "A1 = 1; i >= 2인 경우 A(j) 는 A(j-1) 의 배수" 인 걸 알아야해!!!!
##############################################
import sys


coin_cnt, coin_sum = map(int, sys.stdin.readline().split())

InputList = [int(sys.stdin.readline().strip()) for i in range(coin_cnt)]

result = 0


for i in range(coin_cnt-1, 0, -1):
    a = coin_sum // InputList[i]

    if a == 0:
        continue
    else:
        result += a
        coin_sum -= a*InputList[i]

print(result)