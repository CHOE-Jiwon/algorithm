# 작성일: 2022-07-21
# 문제 링크: https://www.acmicpc.net/problem/10158
# 1 try: 시간 초과 + 구현하는데 너무 오래 걸림.
# 2 try: 방향에 대한거는 신경쓰지 말고 지도를 뚫고 나간 다음에 계산하면 됨.
##############################################
import sys


x, y = map(int, sys.stdin.readline().split())

ant_x, ant_y = map(int, sys.stdin.readline().split())

t = int(sys.stdin.readline())

moved_x = ant_x + t
moved_y = ant_y + t

if (moved_x // x) % 2 == 0:
    result_x = moved_x % x
else:
    result_x = x - moved_x % x

if (moved_y // y) % 2 == 0:
    result_y = moved_y % y
else:
    result_y = y - moved_y % y

print(result_x, result_y)