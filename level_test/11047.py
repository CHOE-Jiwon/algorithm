# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/11047
# 1 try: for 문으로 푸니까 틀렸다고 나왔음. -> coin_sum이 0이 된 이후에도 
##############################################
import sys
from collections import deque


coin_cnt, coin_sum = map(int, sys.stdin.readline().split())

InputList = deque([int(sys.stdin.readline().strip()) for i in range(coin_cnt)])

result = 0

while coin_sum != 0:
    coin = InputList.pop()
    a = coin_sum // coin

    if a == 0:
        continue
    else:
        result += a
        coin_sum -= a*coin

print(result)