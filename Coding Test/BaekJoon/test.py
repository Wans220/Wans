import sys

s = sys.stdin.readline().strip()
if s[0:4] == 'push':
    a = s[0:4]
    b = int(s[5:len(s)])
    
