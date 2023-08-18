# sol_1

import sys

N, M = list(map(int, sys.stdin.readline().split()))
for n in range(N, M+1):
    chk = True
    if n == 1:
        chk = False
    else:
        for div in range(2, int(n**0.5)+1):
            if n%div ==0:
                chk = False
                break;
    print(n) if chk else 1