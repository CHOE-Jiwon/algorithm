# 작성일: 2022-07-24
# 문제 링크: https://www.acmicpc.net/problem/1987
# 1 try: 시간 초과
# 2 try: 뭐
# 3 try: max_cnt == 26일 때 탈출 조건 추가 & pypy3로 돌림
# BFS로 짜본다면 python3로 제출해도 통과할 수 있을듯...
# https://velog.io/@nathan29849/BAEKJOON-1987-%EC%95%8C%ED%8C%8C%EB%B2%B3-DFS-python
##############################################
import sys
import time
from collections import deque

R, C = map(int, sys.stdin.readline().split())

board = [None]*R
visited = deque([False]*26)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_cnt = -1
cnt = 0

def dfs(x, y):
    global max_cnt
    global visited
    global cnt

    # 알파벳 체크 & 카운트 +1
    visited[ord(board[x][y])-65] = True
    cnt += 1

    # max_cnt 업데이트
    if max_cnt < cnt: max_cnt = cnt
    if max_cnt == 26: return

    # 상우좌하 dfs
    for i in range(4):
        # 좌표 미리 구하기
        nx = x + dx[i]
        ny = y + dy[i]

        # 좌표가 정상 범위를 벗어나지 않은 경우 & 방문한 적이 없는 알파벳인 경우
        if nx >= 0 and nx < R and ny >= 0 and ny < C and visited[ord(board[nx][ny])-65] == False:
            dfs(nx, ny)

    # 상하좌우 모두 방문하고 더이상 갈 곳이 없다면 빠져나오기
    # 카운트 -1
    visited[ord(board[x][y])-65] = False
    cnt -= 1


for i in range(R):
    board[i] = list(sys.stdin.readline().strip())

start_time = time.time()


dfs(0, 0)

print(max_cnt)