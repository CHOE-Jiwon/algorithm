# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/1759
# combinations 쓰지 말고 다시 풀어보기...
##############################################
import sys
from itertools import combinations

pw_length, alphabet_cnt = map(int, sys.stdin.readline().split())

alpabet_list = sorted(sys.stdin.readline().split())

vowels_list = ['a', 'e', 'i', 'o', 'u']

combination_list = combinations(alpabet_list, pw_length)

for pw in combination_list:

    vowels_cnt = 0
    consonantants_cnt = 0

    for chr in pw:
        if chr in vowels_list:
            vowels_cnt += 1
        else:
            consonantants_cnt += 1
    
    if vowels_cnt >= 1 and consonantants_cnt >= 2:
        print(''.join(pw))
