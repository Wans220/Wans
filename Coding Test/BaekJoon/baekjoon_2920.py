# sol_1

import sys

clist = sys.stdin.readline().split()
if clist == [str(s) for s in range(1,9)]:
    print("ascending")
elif clist == [str(s) for s in range(8,0,-1)]:
    print("descending")
else:
    print("mixed")
