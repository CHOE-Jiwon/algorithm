# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/1874
##############################################
import sys


testCaseCnt = int(sys.stdin.readline())

answer = list()

for i in range(testCaseCnt):
    InputString = sys.stdin.readline()

    str_len = len(InputString)
    s, e = 0, 1

    result = "YES"

    while s < str_len and e < str_len:
        start_pattern = InputString[s]

        # 0으로 시작할 때는 무조건 01 이어야 함.
        if start_pattern == '0':
            # 00이 나오는 경우 잘못된 패턴
            if InputString[e] != '1':
                result = "NO"
                break
            
            # 패턴이 끝났으면 투 포인터 위치 수정

            print("01 패턴 :: String[{}:{}]".format(s, e))
            s = e + 1
            e += 2
        
        # 1로 시작할 때는 100+1+
        else:

            # 11 이 나오거나 100으로 시작하지 않는다면 잘못된 패턴
            if InputString[e] == '1' or InputString[e:e+2] == '01':
                print(e)
                result = "NO"
                break
            else:
                print("ERR: InputString[e]::{}".format(InputString[e]))
                print("ERR: InputString[e:e+2]::{}".format(InputString[e:e+2]))

            # 0 끝까지 조회
            while InputString[e] == '0':
                e += 1
            
            # 1 끝까지 조회
            while InputString[e] == '1':
                e += 1


            # 마지막 1 다음에 나오는 것이 '00'이면 패턴 끝인데, 그 1이 시작이 되어야 함.
            if InputString[e:e+2] == '00':
                s = e - 1
            # 마지막 1 다음에 나오는 것이 '0'이면 패턴 끝
                print("100+1+ 패턴 :: String[{}:{}] = {}".format(s, e, InputString[s:e]))
            else:
                print("100+1+ 패턴 :: String[{}:{}] = {}".format(s, e, InputString[s:e]))

                s = e
                e += 1
                
    
    answer.append(result)


for i in answer:
    print(i)


print(solution(6, ["3,0,39222100,2020-11-04 02:19:50", "1,0,70403000,2020-12-07 21:41:39", "2,5,89249000,2020-11-15 19:38:21", "0,2,48748300,2021-05-19 14:54:51", "0,5,96059000,2021-05-09 06:40:17", "0,2,16230300,2020-12-13 01:45:17", "3,0,70403000,2020-12-07 21:46:55", "4,5,89249000,2020-11-15 19:45:42", "5,0,72710000,2020-08-08 05:43:18", "4,1,8453500,2020-08-30 20:40:39", "2,5,37973900,2021-06-27 11:40:01", "3,2,71630300,2020-07-19 18:18:49", "5,4,96161000,2020-10-04 07:57:43", "2,3,8796100,2020-08-12 21:28:13", "2,1,71412600,2020-10-24 23:16:07", "4,2,81714500,2021-03-29 17:57:30", "2,0,72710000,2020-08-08 05:34:15", "0,1,92909400,2021-03-05 22:06:42", "4,3,18586200,2020-10-10 04:39:27", "3,5,96059000,2021-05-09 06:47:36", "3,4,96161000,2020-10-04 07:57:21", "5,1,54854500,2020-12-15 05:50:39"]))