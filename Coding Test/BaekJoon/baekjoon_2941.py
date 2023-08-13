# sol_1

import sys

rule = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()
for s in rule:
    word = word.replace(s, "*")
print(len(word))