# sol_1

import sys
import itertools

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    f = [sys.stdin.readline().split() for _ in range(n)]
    f = list(itertools.chain(*f))
    f_num = [int(f[2*i-1]) for i in range(n)]
    index = f_num.index(max(f_num))
    print(f[2*(index-1)])
