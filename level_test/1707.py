# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/1874
##############################################
import sys


testCnt = int(sys.stdin.readline())

for _ in range(testCnt):
    v_cnt, e_cnt = map(int, sys.stdin.readline().split())

    graphs = list()

    for __ in range(e_cnt):
        u, v = map(int, sys.stdin.readline().split())

        graphs.append([u,v])
    
    for x in sorted(graphs, key = lambda x:min(x)):
        print(min(x),max(x))