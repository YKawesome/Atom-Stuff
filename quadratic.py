import numpy as np
listy = list()

while True:
    x = input("Coefficient: ")
    if x == '':
        break
    listy.append(int(x))




y = np.roots(listy)

for root in y:
    print(np.round(root,3))
