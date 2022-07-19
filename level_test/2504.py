# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/2504
# 1 try: 정규표현식 사용. 시간초과
##############################################
import sys
import re

InputString = sys.stdin.readline().strip()

if '[)' in InputString or '(]' in InputString:
    print(0)
else:
    small_p = re.compile('\([0-9]+\)')

    InputString = InputString \
                    .replace(')(', ')+(') \
                    .replace(')[', ')+[') \
                    .replace('](', ']+(') \
                    .replace('][', ']+[') \
                    .replace('()', '2') \
                    .replace('[]','3')

    big_list = InputString.replace(']', '[').split('[')
    for i in range(len(big_list)):
        if i % 2 == 1:
            big_list[i] = str(int(big_list[i])*3)

    InputString = ''.join(big_list)

    small_list = InputString.replace(')', '(').split('(')
    print(small_list)
    for i in range(len(small_list)):
        if small_list[i] not in ['', '+']:
            print(small_list[i])
            InputString = InputString.replace(small_list[i], str(eval(small_list[i])))
            
    while '(' in InputString:

        small_list = small_p.findall(InputString)

        for small in small_list:
            InputString = InputString.replace(small, str(2*(int(small[1:-1]))))

    print(eval(InputString))