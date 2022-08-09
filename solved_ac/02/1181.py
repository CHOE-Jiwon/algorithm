# 작성일: 2022-08-09
# 문제 링크: https://www.acmicpc.net/problem/1181
# 이거 풀었던거임!!!
# python 정렬에 대해서 다시 공부해보자. 팀소트!
##############################################
import sys

testCaseCnt = int(sys.stdin.readline())

tmp_list = list()

for i in range(testCaseCnt):
    word = sys.stdin.readline().strip()

    if word not in tmp_list:
        tmp_list.append(word)

for word in sorted(tmp_list, key=lambda x:(len(x), x)):
    print(word)