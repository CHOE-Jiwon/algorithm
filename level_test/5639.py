# 작성일: 2022-07-29
# 문제 링크: https://www.acmicpc.net/problem/5369
# 얼마나 입력받을지 모를 때 쓰는 코드가 또 있음!
# 첫번째 짜려는 코드는 안될 것 같음
##############################################
import sys
from collections import deque

preorder = list()
while True:
    try:
        preorder.append(int(sys.stdin.readline().strip()))
    except:
        break


tree_dict = dict()

def make_node(left_range, right_range):
    node = {
        "left_range": left_range
        , "right_range": right_range
    }

    return node

## 주의
tree_dict[preorder[0]] = make_node(range(0, preorder[0]), range(preorder[0]+1, 1000001))

active_num_stack = list()
active_num_stack.append(preorder[0])

# dict에서 index로 서치하는 것은 overhead를 발생시킬 수 있다.
for num in preorder[1:]:

    while 1:
        active_num = active_num_stack[-1]
        active_node = tree_dict[active_num]

        if num in active_node["left_range"]:
            tree_dict[num] = make_node(range(active_node["left_range"][0], num), range(num+1, active_num))
            break
        elif num in active_node["right_range"]:
            tree_dict[num] = make_node(range(active_num + 1, num), range(num+1, active_node["right_range"][-1] + 1))
            break
        else:
            print(active_num_stack.pop())

    active_num_stack.append(num)

while active_num_stack:
    print(active_num_stack.pop())