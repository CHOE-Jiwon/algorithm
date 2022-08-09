# 작성일: 2022-08-09
# 문제 링크: https://www.acmicpc.net/problem/1436
##############################################
import sys


rank = int(sys.stdin.readline())

answer = str(rank - 1) + "666" if rank != 1 else "666"

print(answer)
