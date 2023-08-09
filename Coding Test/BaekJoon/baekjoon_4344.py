# sol_1

answer_ary = []
for _ in range(int(input())):
    score_ary = list(map(int, input().split()))
    avg = (sum(score_ary) - score_ary[0])/score_ary[0]
    proportion = 0
    for i in range(score_ary[0]):
        if score_ary[i+1] > avg:
            proportion += 1
    answer_ary.append(proportion/score_ary[0])    
[print("%f%%" %(s*100)) for s in answer_ary]
    
