n = int(input("Enter number of elements : "))
listinput = list(map(int,input("\nEnter the numbers split by a space: ").strip().split()))[:n] 

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def threefour(listy):
    new = listy
    for index,item in enumerate(listy):
        if item == 3:
            if 4 in new[index:]:
                new = swapPositions(new,index+1,new[index:].index(4)+index)
    return new

print(threefour(listinput))
