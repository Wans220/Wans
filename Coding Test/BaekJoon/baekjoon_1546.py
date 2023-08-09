# sol_1 
a = int(input())
new_score = []
score_ary = list(map(int, input().split()))
max_score = max(score_ary)

for i in range(a):
    new_score.append(score_ary[i]/max_score*100)
print(sum(new_score)/a)