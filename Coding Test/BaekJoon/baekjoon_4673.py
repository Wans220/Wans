# sol_1

def self_num(num):
    return num + sum(map(int, str(num)))
    
ary = [] * 10000
for i in range(1,10001):
    ary.append(self_num(i))
for i in range(1,10000+1):
    if i not in set(ary):
        print(i)
