# sol_1 -- 재귀로 풀었으나 시간초과

import sys
def q(k , n):
    rt = 0
    for i in range(n+1):
        if k == 0:
            rt = i
        else:
            rt = rt + q(k-1, i)            
    return rt

answer = []
N = int(sys.stdin.readline())
for ㅑ in range(N):
    k, n = [int(sys.stdin.readline().strip()) for _ in range(2)]
    answer.append(q(k,n))
[print(s) for s in answer]    


# sol_2 -- 반복문을 사용

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    k, n = [int(sys.stdin.readline().strip()) for _ in range(2)]
    answer = [i for i in range(1, n+1)]
    for x in range(k):
        for y in range(1, n):
            answer[y] = answer[y] + answer[y-1]
    print(answer[-1])
