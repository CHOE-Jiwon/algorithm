# 작성일: 2022-07-24
# 문제 링크: https://www.acmicpc.net/problem/2436
# 에라토스테네스 - 소인수분해법 공부
# 소인수 + 최소합
##############################################
# 정석 해결법
# 최소공배수 = A x B x 최대공약수인 점을 가지고 A X B의 범위를 구하고
# 1 ~ (AxB)//2 + 1의 범위를 순회하면서
# 약수 쌍을 구한 후 (예를 들어 1-24 / 2-12 / 3-8 / 4-6 ) 합을 비교하여 결과 업데이트
##############################################
import sys
from collections import Counter
from itertools import combinations

gcd, lcm = map(int, sys.stdin.readline().split())


# 효율적인 소인수 분해
def factorize(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = int(n // factor)  # n을 몫으로 변경
        factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append -> 2,3 경우
        factors.append(n)
    
    return factors

tmp_list = factorize(lcm / gcd)
counter = Counter(tmp_list)
new_list = [x**counter[x] for x in counter]

min_sum = 200000000
result = [gcd, lcm]

for i in range(1, len(new_list)//2+1):
    a = combinations(new_list, i)

    for l in a:
        b = eval('*'.join(map(str,l)))
        c = eval('*'.join(map(str,list(set(new_list) - set(l)))))

        if (b+c) < min_sum:
            min_sum = b+c
            result[0] = min(b, c) * gcd
            result[1] = max(b, c) * gcd

print(*result)
