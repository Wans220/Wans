# # sol_1 부끄러운 무식한방법 이거밖에 생각안남...

# import sys

# N = int(sys.stdin.readline())
# if N % 5 == 0:
#     print(N // 5)
# else:
#     num = 0
#     while N > 0:
#         N = N - 3
#         num += 1
#         if N % 5 == 0:
#             print(num + N//5)
#             break;
#         elif N == 1 or N == 2:
#             print(-1)
#             break;
#         elif N == 0:
#             print(num)
#             break;
        
# sol_2  - dp

import sys

N = int(sys.stdin.readline())
dp = [-1 for _ in range(5001)]
dp[3], dp[5] = 1, 1

if N <= 5:
    print(dp[N])
else:
    for i in range(6, N+1):
        a, b = dp[i], dp[i]
        
        if dp[i-5] != -1:
            a = dp[i-5]
        if dp[i-3] != -1:
            b = dp[i-3]
        if a > 0 and b > 0:
            dp[i] = min(a+1, b+1)
        elif a > 0 and b < 0:
            dp[i] = a + 1
        elif a < 0 and b > 0:
            dp[i] = b + 1
        else:
            dp[i]= -1
    print(dp[N]) 
                