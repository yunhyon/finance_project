import math #math herin is a python module
li = [5, 2, 14, 9, 2]
sum = 0
for elem in li:
    sum = elem + sum

avg = sum/len(li)
print(math.sqrt(1/len(li)*(elem-avg)*(elem-avg)))


sentence = 'This is a very historical moment!'
print(sentence)