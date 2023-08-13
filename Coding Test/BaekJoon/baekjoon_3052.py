# sol_1

import sys

n_list = [int(sys.stdin.readline().strip()) for _ in range(10)]
mod = []
for n in n_list:
    mod.append(n%42)
print(len(set(mod)))
