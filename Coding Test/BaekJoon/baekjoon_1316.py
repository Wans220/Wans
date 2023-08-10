# sol_1

import sys

N = int(sys.stdin.readline())
group_word = N
for _ in range(N):
    word = sys.stdin.readline().strip()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue;
        elif word[i] in word[i+1:]:
            group_word -= 1
            break;
print(group_word)
    