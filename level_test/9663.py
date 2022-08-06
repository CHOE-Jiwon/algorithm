# 작성일: 2022-08-03
# 문제 링크: https://www.acmicpc.net/problem/9663
# 1 try: 2 시간동안 풀어보려고 했으나 실패!
##############################################
import sys

sys.setrecursionlimit(10**6)

N = int((sys.stdin.readline()))

result = 0

def dfs(x, y, start):

    global result


    print(x+1, y+1, visited)
    # 현재 좌표가 마지막 좌표라면 방문 여부에 상관없이 끝.
    if not start and x+1 == N and y+1 == N:
        result += 1
        return

    if start == True:
        start = False

    # 방문한 적이 없는 좌표라면
    if not visited[x+1][y+1]:


        # 해당 좌표가 마지막 좌표가 아니라면.
        # 1. 같은 row 전부 방문으로 바꾸고
        for k in visited[x+1]:
            visited[x+1][k] = 1
        
        # 2. 같은 column 전부 방문으로 바꾸고
        for k in visited:
            visited[k][y+1] = 1
        
        # 좌표 이동 범위 생성 후
        move = [x for x in range(-N+1, N)]
        # 3. 좌상단, 우하단을 가로지르는 대각선 전부 방문으로 바꾸고
        for i in move:
            nx = (x+1) + i
            ny = (y+1) + i

            if nx > 0 and nx <= N and ny > 0 and ny <= N:
                visited[nx][ny]=1

        # 4. 우상단, 좌하단을 가로지르는 대각선 전부 방문으로 바꾸고
        for i in move:
            nx = (x+1) + i
            ny = (y+1) - i

            if nx > 0 and nx <= N and ny > 0 and ny <= N:
                visited[nx][ny]=1

        # 5. 나머지 점에서 다시 조회
        for i in range(N):
            for l in range(N):
                dfs(i, l, start)
        
    # 방문한 적이 있으면 빠져나오기
    else:
        return




# 보드 전체를 다 돌면서
for i in range(N):
    for l in range(N):
        # 특정 점에서 시작하기 전에 visited 생성하고
        visited = {x+1:{y+1:0 for y in range(N)} for x in range(N)}

        start = True
        print("START::", i+1, l+1)
        dfs(i, l, start)
        print("RESULT::", result)

print(result)