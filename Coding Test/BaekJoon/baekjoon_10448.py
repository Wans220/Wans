# sol_1

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    find_num = int(sys.stdin.readline())
    trign = [0] * 1001
    
    Tn = [int(i*(i+1)/2) for i in range(1,46)]
    for i in Tn:
        for j in Tn:
            for k in Tn:
                if trign[min(1000, i+j+k)] ==1:
                    continue
                else:
                    trign[min(1000, i+j+k)] = 1
    print(trign[find_num])