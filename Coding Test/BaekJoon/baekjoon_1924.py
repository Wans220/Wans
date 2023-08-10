# sol_1 - 직관적이지만 음...다른 방법으로

import sys

day = 0
x, y = map(int, sys.stdin.readline().split())
for i in range(1,x):
    if i in [1,3,5,7,8,10,12]:
        day += 31
    elif i in [4,6,9,11]:
        day += 30
    elif i == 2:
        day += 28
day = (day+y-1)%7
if day == 0:
    print("MON")
elif day == 1:
    print("TUE")
elif day == 2:
    print("WED")
elif day == 3:
    print("THU")
elif day == 4:
    print("FRI")
elif day == 5:
    print("SAT")
elif day == 6:
    print("SUN")


# sol_2

import sys
day = 0
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["MON","TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, sys.stdin.readline().split())

for i in range(x-1):
    day += dayList[i]
day = (day+y-1)%7
print(weekList[day])



# sol_3 - calendar module 사용

import calendar
import sys
weekList = ["MON","TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, sys.stdin.readline().split())
day = calendar.weekday(2007, x, y)
print(weekList[day])
