# sol_1

import sys
N = int(sys.stdin.readline())
ary = [0] * 100

for i in range(1, N+1):
    if i ==1:
        ary[i] = 1
    else:
        ary[i] = ary[i-1] + ary[i-2]
print(ary[N])