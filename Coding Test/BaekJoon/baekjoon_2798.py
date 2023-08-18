# sol_1

import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
ary = list(map(int, sys.stdin.readline().split()))
sum_list = []
for i in permutations(ary, 3):
    sum_list.append(sum(i))

sum_list = list(set(sum_list))
sum_list_aft = [sum_list[i] for i in range(len(sum_list)) if sum_list[i] <= M]
print(max(sum_list_aft))