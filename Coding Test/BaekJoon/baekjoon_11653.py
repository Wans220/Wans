# sol_1

import sys
n = int(sys.stdin.readline())
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = int(n / i)
