# 작성일: 2022-08-01
# 문제 링크: https://www.acmicpc.net/problem/1707
# 그래프를 만들고 -> 첫번째 노드부터 BFS든 DFS든 해보자.
# 1시간 넘게 고민해보았으나 답이 안나왔음. 구글링시작~
# https://ji-gwang.tistory.com/293 -> 여기서는 graph를 2차원 배열로
# 내 초기 풀이 방법은 graph를 dictionary로 구현하는 것이었다. 여기까지는 괜찮았지만, 이거 말고 문제 많았음.
# 풀이에서, 방문하지 않은 노드를 처음에 무조건 1로 설정하는데 왜 이게 문제가 없는걸까? -> 서로 별개의 그룹으로 보는것임.
# 내가 초기에 하려던 방법이 알고보니 BFS 느낌인데???
##############################################
import sys
from collections import deque

sys.setrecursionlimit(10**6)

testCnt = int(sys.stdin.readline())

def bfs(u, color):
    queue = deque([u])
    colors[u] = color

    while queue:
        popped = queue.popleft()

        for i in graphs[popped]:
            if not colors[i]:
                queue.append(i)
                colors[i] = -1 * colors[popped]
            elif colors[i] == colors[popped]:
                return False

    return True


for _ in range(testCnt):
    v_cnt, e_cnt = map(int, sys.stdin.readline().split())

    graphs = dict()
    colors = [False] * (v_cnt + 1)

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
    
    for v in graphs:
        
        # 만약 방문하지 않은 정점이라면 dfs 시작
        if not colors[v]:

            # 방문하지 않은 정점에 대해서 color는 1로 설정.
            result = bfs(v, 1)

            if not result:
                break
    
    print("YES" if result else "NO")
