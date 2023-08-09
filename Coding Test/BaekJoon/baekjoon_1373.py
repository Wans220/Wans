# sol_1 반복문 이용  --> 시간초과
def change_num(num, digits):
    ten_num = 0
    conv_num = ''
    for i in range(len(num)):
        ten_num += int(num[-1])*(2**i)
        num = num[:-1]
    while ten_num != 0:
        conv_num += str(ten_num%digits)
        ten_num = ten_num // digits
    return conv_num[::-1]
num = input()
print(change_num(num, 8))
        
# sol_2 내장함수
print(oct(int(input(),2))[2:])