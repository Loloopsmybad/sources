# **Problem 7**
# Find the length of the longest contiguous subarray with **all distinct** elements (i.e. no
# duplicates). Use the sliding-window (two-pointer) technique.
# **Test Cases:**
# 1. Input: `[5, 1, 3, 5, 2, 3, 4, 1]` → Output: `5`
# 2. Input: `[1, 2, 3, 4, 5]` → Output: `5`
# 3. Input: `[1, 1, 1, 1]` → Output: `1`
def congi(arr):
    i=1
    c=0
    a=[]
    count=0
    col=[]
    for j in arr:
        print("changed j", j)
        while i<len(arr) and arr[i] not in a :
            if arr[i]!=j:
                a.append(arr[i])
                print("hi")
                i+=1
                c+=1
                count+=1
            elif arr[i]==j:
                a.append(arr[i])
                i+=1
                c+=1
                break
        print ("value of i",i)
        i=(i-c)+1
        c=0
        print ("value of i",i)
        print("count",count+1)
        col.append(count+1)
        print(col)
        count=0
        a=[]
        if i == len(arr):
            break
        
    print(max(col))

congi([5, 1, 3, 5, 2, 3, 4, 1])