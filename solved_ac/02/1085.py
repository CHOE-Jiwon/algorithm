# 작성일: 2022-08-09
# 문제 링크: https://www.acmicpc.net/problem/1085
##############################################
import sys


x, y, w, h = map(int, sys.stdin.readline().split())

distances = [x, y, w-x, h-y]

print(min(distances))