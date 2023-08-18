# sol_1

import sys

N = int(sys.stdin.readline())
ary = [sys.stdin.readline().strip() for _ in range(N)]
size = []
for s in ary:
    size.append(len(s))
sort_ary = []

for n in list(set(sorted(size))):
    temp_ary = []
    for s in ary:
        if len(s) == n:
            temp_ary.append(s)
    sort_ary += sorted(list(set(temp_ary)))
[print(s) for s in sort_ary]
