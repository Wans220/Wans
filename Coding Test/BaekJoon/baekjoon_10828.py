# sol_1

def user_command(ary, com_nm, num):
    if com_nm == 'push':
        ary.append(num)
    elif com_nm == 'top':
        print(-1) if len(ary) == 0 else print(ary[len(ary)-1])
    elif com_nm == 'size':
        print(len(ary))
    elif com_nm == 'empty':
        print(1) if len(ary) == 0 else print(0)
    elif com_nm == 'pop':
        if len(ary) == 0:
            print(-1)
        else:
            print(ary[len(ary)-1])
            ary = ary[:len(ary)-1]
    return ary       

def read_command(s):
    a = s[0:4]
    if a == 'push':
        b = int(s[5:len(s)])
    else:
        a = s
        b = 0
    return a, b

    
import sys
ary = []
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = read_command(sys.stdin.readline().strip())
    ary = user_command(ary=ary, com_nm=a,num=int(b))
