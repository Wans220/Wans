# sol_1

import sys

N = int(sys.stdin.readline())
ary = [int(sys.stdin.readline().strip()) for _ in range(N)]
[print(s) for s in sorted(ary)]