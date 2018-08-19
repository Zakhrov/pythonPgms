scores={}
res_f=open("scorefile.txt")
for line in res_f:
    (name,score)=line.split()
    scores[score]=name
res_f.close()
print("the scores are")
for each_score in sorted(scores.keys(),reverse=True):
    print("surfer " + scores[each_score] + " scored " + each_score)
    print("top scores")
    
