# 작성일: 2022-07-17
# 문제 링크: https://www.acmicpc.net/problem/1966
##############################################
import sys
from collections import deque

testCase = int(sys.stdin.readline())

for i in range(testCase):
    
    paper_cnt, target = map(int, sys.stdin.readline().split())

    priority_list = deque([int(x) for x in sys.stdin.readline().split()])
    paper_queue = deque([i for i in range(paper_cnt)])

    result = 0
    
    while paper_queue:

        curr_paper = paper_queue[0]
        priority = priority_list[0]

        if priority < max(priority_list):
            paper_queue.append(paper_queue.popleft())
            priority_list.append(priority_list.popleft())
        else:
            result += 1

            paper_queue.popleft()
            priority_list.popleft()

            if curr_paper == target:
                print(result)
                break
