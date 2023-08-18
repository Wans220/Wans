# sol_1

import sys
def comp(n):
    return int(n + sum(map(int, str(n))))

N = int(sys.stdin.readline())
ary = []
for i in range(N, 0 -1):
    if N == comp(i):
        ary.append(i)
if len(ary) == 0:
    print(0)
else:
    print(min(ary))

# sol_2 -- 1을 개선 -- 런타임오류 왜일까>?

import sys
import math
def comp(n):
    return int(n + sum(map(int, str(n))))

N = int(sys.stdin.readline())
ary = []
for i in range(N, N - int(math.log10(N)+1)*10, -1):
    if N == comp(i):
        ary.append(i)
if len(ary) == 0:
    print(0)
else:
    print(min(ary))
