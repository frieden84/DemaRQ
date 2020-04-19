predFile='predictions.tsv'
goldFile='gold.txt'

with open(predFile) as f:
    predictions = f.readlines()
with open(goldFile) as f:
    gold = f.readlines()

tp=0.0
total=0.0
for i in range(0, len(predictions)):
    if predictions[i].split("\t")[0].strip()=='REQUIREMENT':
        found = predictions[i].split("\t")[1]
        total=total+1
        for j in range(0, len(gold)):
            if found==gold[j]:
                tp=tp+1
                break

precision = (tp/total)*100
recall = (tp/(1.0*len(gold)))*100
print 'precision = %1.0f %%' % precision
print 'recall = %1.0f %%' % recall