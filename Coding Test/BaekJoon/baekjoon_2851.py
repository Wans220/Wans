# sol_1

import sys
mush = [int(sys.stdin.readline().strip()) for _ in range(10)]
target = [0] * 10
index = 0
for i in range(10):
    target[i] = target[max(0, i-1)] + mush[i]
    if (index == 0 and target[i] >= 100):
        index = i
try:
    if (abs(target[index] - 100) <= abs(target[index-1] - 100)):
        print(target[index])
    else:
        print(target[index-1])
except:
    print(target[index])        


# sol_2

ans,score = 0,0
for i in range(10):
    score+=int(input())
    if 100-ans >= abs(100-score):
        ans = score
print(ans)

