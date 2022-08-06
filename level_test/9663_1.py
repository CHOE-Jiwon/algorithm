# 작성일: 2022-08-03
# 문제 링크: https://www.acmicpc.net/problem/9663
# 1 try: 2 시간동안 풀어보려고 했으나 실패!
# 사람들 풀이를 보자
# 1. 퀸은 하나의 row에 같이 존재할 수가 없다. 따라서 우리가 보드판을 2차원 배열로 만들지 않고 1차원 배열로 표현이 가능하.
#   -> board[1] = 5 : 1번째 row의 5번째 컬럼에 퀸이 존재한다 라는 뜻.
# 2. [x, y]에 Queen을 놓을 수 있는지 확인하는 함수 생성
#   -> 원래는 같은 행, 같은 열, 대각선 방향을 검사해야 하지만
#   -> 우리가 1번에서 정의한대로라면 같은 행은 검사할 필요가 없음. (애시당초 같은 행에 놓을 로직을 안만듦)
#   -> 그러면 같은 열, 대각선만 검사하면 됨.
#      -> 같은 열 검사
#           board[x]가 재귀를 시작한 board[r]과 값이 동일하면 안됨. (동일하다는건 놓으려는 놈이랑, 그 전에 놓은 놈이 같튼 열에 있다는 뜻.)
#      -> 대각선 검사(좌상-우하)
#           우리가 시작을 제일 첫번째 row, 첫번째 column 부터 -> N번째 row, N 번째 column 까지 재귀를 갈거임.
#           이 말인 즉슨, 좌상만 보면 된다. 우하는 아직 놓지 않았기 때문(좌상단 놈들한테 공격 안받는지 확인하는 것).
#      -> 대각선 검사(우상-좌하)
#           우리는 우상만 보면된다. 좌하는 아직 놓지 않았기 때문.
#      -> 이거를 코드로 표현하면
#           abs(row[x] - row[i]) == abs(x-i)
# 3. 첫번째 row 부터 N 번째 row 까지 각 column을 재귀로 돌면서 N-Queen 진행.
##############################################
import sys

sys.setrecursionlimit(10**6)

N = int((sys.stdin.readline()))

result = 0

board = [0] * (N+1)

def isPromising(x):

    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
        
    return True

def dfs(x):
    global result

    # 마지막 행을 본다는건 그 행의 어떤 열에 놓든, 놓지 못하든 끝까지 찾아봤다는 것!
    if x == N:
        result += 1
        return
    
    else:
        # 하나의 행(x)에서 각 열(i)에 Queen을 놓고싶은데.
        for i in range(N):
            row[x] = i

            # 만약 놓을 수 있다면 놓고 다음행 시작 (x+1, y)
            if isPromising(x):
                dfs(x+1)
            # 못 놓는다면 다음 열 시작 (x, y+1)

dfs(0)
print(result)