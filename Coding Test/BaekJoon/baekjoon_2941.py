# sol_1

import sys

change_rule = {'c=' : '1', 'c-' : '2', 'dz=' : '3', 'd-' : '4', 'lj' : '5', 'nj' : '6', 's=' : '7', 'z=' : '8'}
rule_key = ''.join(list(change_rule.keys()))
rule_value = ''.join(list(change_rule.values()))
chk = chk.translate(chr.make)
chk = sys.stdin.readline().strip()

chk = chk.translate
print(chk)


