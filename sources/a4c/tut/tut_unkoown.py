def palindrme(arr,cut):
    if len(arr)<=1:
        return a
        
    mid=len(arr)//2    
    left=palindrme(arr[:mid])
    right=palindrme(arr[mid:])

    
    i=0
    j=len(right)-1
    m=[]
    while j >= 0 :
        if left[i]==right[j]:
            i+=1
            j-=1
            cut+=1
        else:
            i+=1
            j-=1
    m=left+right


    return m,cut
    
stri = input("nigger")
cut=0
palindrme(stri)