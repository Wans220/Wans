# sol_1

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    str = sys.stdin.readline().split()
    new_s = []
    for s in str:
        new_s.append(s[::-1]) 
    print(' '.join(new_s))