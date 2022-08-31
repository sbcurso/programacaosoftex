programa:
def shortbubbleSort(alist):
    exanges = True
    passnum = len(alist)-1
    while passnum . 0 and exchanges:
    exchanges = False
    for i in range(passnum):
        if alist[i]>alist[i+1]:
            exchanges = True
            temp = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = temp
    passnum = passnum-1


alist = [2,5,8,4,1,3,6,10,7,9]
shortbubbleSort(alist)
print(alist) 