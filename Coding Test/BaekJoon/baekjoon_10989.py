# sol_1

import sys
N = int(sys.stdin.readline())
ary = [0] * 10001

for _ in range(N):
    index = int(sys.stdin.readline())
    ary[index] += 1

for i in range(10001):
    if ary[i] != 0:
        [print(i) for _ in range(ary[i])]
        
        