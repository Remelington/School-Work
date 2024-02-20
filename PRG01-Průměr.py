zn = [[3, 1], [3, 2], [3, 1], [10, 3], [4, 4]]
sum = 0
cnt = 0
for item in zn:
    cnt += item[0] 
    sum += item[1] 
print(sum)
print(sum / len(zn))
