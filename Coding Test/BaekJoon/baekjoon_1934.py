# sol_1

def find(a,b):
    for i in range(min(a,b)+1,0,-1):
        if ((a%i)==0 and (b%i)==0):
            return i

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a*b/find(a,b)))