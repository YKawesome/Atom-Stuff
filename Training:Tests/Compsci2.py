x = [2,2,11,4,9,7,9]
max = max(x)
for index, item in enumerate(x):
    y = x[:index]+x[index:]
    print(y)
