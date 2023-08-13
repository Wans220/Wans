# sol_1

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    a = sys.stdin.readline().strip()
    cnt = [0] * len(a)
    for i in range(len(a)):
        if i == 0 and a[0] == 'O':
            cnt[i] = 1
        elif a[i] == 'O':
            cnt[i] = cnt[i-1] + 1
    print(sum(cnt))

