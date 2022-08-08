# 작성일: 2022-08-08
# 문제 링크: https://www.acmicpc.net/problem/1018
##############################################
import sys


M, N = map(int, sys.stdin.readline().split())

board = ['']*M

for i in range(M):
    board[i] = sys.stdin.readline().strip()

answer = 63

board_w = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
]

board_b = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]

def howManyChange(board, start):

    cnt = 0

    for i in range(8):
        for j in range(8):
            if start == 'w' and board_w[i][j] != board[i][j]:
                cnt += 1
            if start == 'b' and board_b[i][j] != board[i][j]:
                cnt += 1

    return cnt



for i in range(0, M-7):
    for j in range(0, N-7):
        tmp_board = [[board[x][y] for y in range(j, j+8)] for x in range(i, i+8)]
        
        w_cnt = howManyChange(tmp_board, 'w')
        b_cnt = howManyChange(tmp_board, 'b')

        if w_cnt < answer : 
            answer = w_cnt
        if b_cnt < answer :
            answer = b_cnt

print(answer)