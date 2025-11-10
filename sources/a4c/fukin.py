def chek(arr1,arr2):
    arr1=set(arr1)
    arr2=set(arr2)
    arr1=list(arr1)
    arr2=list(arr2)
    m=[]
    for i in arr1 :
        if i not in arr2 :
            m.append(i)
    for i in arr2 :
        if i not in arr1 :
            m.append(i)
    print(m)
chek([1,2,2,3,4,5],[1,1,1,2,3,6])