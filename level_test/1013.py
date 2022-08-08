# 작성일: 2022-08-07
# 문제 링크: https://www.acmicpc.net/problem/1013
# 1 try: 열심히 풀었는데 틀림!
# 2 try: 사람들은 다 정규식으로 풀었네?
# DFA ???? 상태 전이도 ???
##############################################
import sys


testCaseCnt = int(sys.stdin.readline())

answer = list()

for i in range(testCaseCnt):
    InputString = sys.stdin.readline().strip()

    str_len = len(InputString)
    s, e = 0, 1

    result = "YES"

    while e < str_len:

        # 0으로 시작할 때는 무조건 01 이어야 함.
        if InputString[s] == '0':

            # 00이 나오는 경우 잘못된 패턴
            # 또는 시작이 0인데, 그게 마지막 글자일 경우.
            if InputString[e] != '1' or s == str_len - 1:
                result = "NO"
                break
            
            # print("01 패턴 :: String[{}:{}] = {}".format(s, e, InputString[s:e+1]))

            # 패턴이 끝났으면 투 포인터 위치 수정
            s = e + 1
            e += 2
        
        # 1로 시작할 때는 100+1+
        else:

            # 100+1+ 패턴은 최소한 4개의 글자가 필요하지만 그게 어긋난 경우
            # 11 이 나오거나 100으로 시작하지 않는다면 잘못된 패턴
            if s >= str_len - 3 or InputString[e:e+2] != '00':
                result = "NO"
                break

            # 0 조회
            while e < str_len - 1 and InputString[e] == '0':
                e += 1

            # 1이 나올때까지 조회하고 싶었으나 그 전에 문자열이 끝난 경우
            if InputString[e] == '0':
                result = "NO"
                break
            
            # 1 끝까지 조회
            while e <= str_len - 1 and InputString[e] == '1':
                e += 1

            
            # print("100+1+ 패턴 :: String[{}:{}] = {}".format(s, e-1, InputString[s:e]))

            # e+1이 존재하고 
            if e+1 <= str_len - 1:
                # e+1이 1이라면 01 패턴이 되는것.
                if InputString[e+1] == '1':
                    s = e
                    e += 1
                # 100+1+ 패턴이라면
                else:
                    # 이전 패턴의 1+가 "1" 이었다면 시작값을 e로
                    if InputString[e-2] == '0':
                        s = e
                        e += 1
                    # 이전 패턴의 1+가 "11..." 이었다면 시작값을 e-1로
                    else:
                        s = e-1
                
    
    answer.append(result)


for i in answer:
    print(i)