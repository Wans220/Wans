# sol_1

import sys

N = int(sys.stdin.readline())
cnt = 1
while N >1 :
    N = N - cnt * 6 
    cnt += 1
print(cnt)
