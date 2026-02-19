def pal(list):
    i=len(list)-2
    a=list.copy()
    while i!=-1 :
        a.append(list[i])
        i-=1
    print(a)
pal([1,2,3,4])