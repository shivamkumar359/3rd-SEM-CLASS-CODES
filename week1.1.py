# Sum of numbers greater than 25 in tempt

tempt = [30,32,54,21,16,25,44,78]
avg = sum(tempt)/len(tempt)
count = 0
for t in tempt :
  if t>25:
    count+= t
print(count)
