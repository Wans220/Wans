# sol_1

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    s = sys.stdin.readline().strip()
    for _ in range(len(s)):
        s = s.replace('()','')
    if s == '':
        print("YES")
    else:
        print("NO")
