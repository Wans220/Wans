# sol_1

def fib1(n):
    global cnt1
    if (n==1 or n==2):
        return 1;
    else:
        cnt1 += 1
        return (fib1(n-1)+fib1(n-2));
def fib2(n):
    global cnt2
    f = [1] * (n+1)
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]
N = int(input())
cnt1 = 1
cnt2 = 0
fib1(N)
fib2(N)
print(cnt1, cnt2)