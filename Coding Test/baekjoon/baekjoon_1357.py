# sol_1 처음 생각난 방식
  
def rev(num):
    size = 0
    while 1:
        if num < pow(10, size):
            break
        size += 1
    ary = []
    for i in range(0,size):
        ary.append(num//pow(10, size-i-1))
        num = num - (num//pow(10, size-i-1))*pow(10,size-i-1)
    if size == 1:
        return ary[0]
    elif size == 2:
        return ary[1]*10 + ary[0]*1
    elif size == 3:
        return ary[2]*100 + ary[1]*10 + ary[0]
    else:
        return ary[3]*1000 + ary[2]*100 + ary[1]*10 + ary[0]
a, b = map(int ,input().split())
print(int(rev(rev(a)+rev(b))))

# sol_2 슬라이싱 

a,b = input().split()
a = int(a[::-1]) 
b = int(b[::-1]) 
print(int(str(a+b)[::-1])) 