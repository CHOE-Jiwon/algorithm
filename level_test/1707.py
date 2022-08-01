# 작성일: 2022-08-01
# 문제 링크: https://www.acmicpc.net/problem/1707
# 그래프를 만들고 -> 첫번째 노드부터 BFS든 DFS든 해보자.
##############################################
import sys
from collections import deque

testCnt = int(sys.stdin.readline())

for _ in range(testCnt):
    v_cnt, e_cnt = map(int, sys.stdin.readline().split())

    graphs = dict()

    # graph 생성
    for __ in range(e_cnt):
        u, v = map(int, sys.stdin.readline().split())

        if u not in graphs:
            graphs[u] = [v]
        else:
            graphs[u].append(v)
        
        if v not in graphs:
            graphs[v] = [u]
        else:
            graphs[v].append(u)
    
    queue = deque()
    colors = dict()
    for k, v in graphs.items():
        
