# **Problem 6**
# You are given a list of non-empty strings (words). Group the words that are anagrams of
# each other. Return a list of groups, where each group is a lexicographically sorted list of its
# words. The list of groups itself should be sorted by:
# 1. Descending group size (largest group first)
# 2. If two groups have same size, then by lexicographically smallest member
# 3. Within each group, sort the words lexicographically
# **Test Cases:**
# 1. Input: `["eat", "tea", "tan", "ate", "nat", "bat", "tab", "abt"]` → Output: `[["abt","bat","tab"],
# ["ate","eat","tea"], ["nat","tan"]]`
# 2. Input: `["listen", "silent", "enlist", "google", "gooegl", "abc"]` → Output:
# `[["enlist","listen","silent"], ["google","gooegl"], ["abc"]]`
# 3. Input: `["a", "b", "ab", "ba", "abc", "cba", "bac"]` → Output: `[["abc","bac","cba"], ["ab","ba"],
# ["a"], ["b"]]`

def anagram(arr):
    lst=arr.copy()
    for i in range(len(lst)):
        lst[i]=list(lst[i])
        lst[i].sort()
    merged=[]

    left=0
    right=len(arr)-1
    m=[]
    while left<=len(lst)-1:
        if lst[left]==lst[right]:
            m.append(arr[right])
            right-=1
        else:
            right-=1
        if right<0:
                merged.append(m)
                m=[]
                right=len(arr)-1
                left+=1
    merged=set(tuple(x) for x in merged)
    merged=[list(x) for x in set(tuple(x) for x in merged)]
    # merged.sort()
    for i in merged:
        i.sort()
    print("prev==>",merged)
    print(mergsort(merged))

def mergsort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left= mergsort(arr[:mid])
    right= mergsort(arr[mid:])

    i=j=0
    m=[]
    while i <len(left) and j < len(right):
        if len(left[i]) > len(right[j]):
            m.append(left[i])
            i+=1
        elif len(left[i]) < len(right[j]):
            m.append(right[j])
            j+=1

        else:
            if left[i] > right[j]:
                m.append(right[j])
                j+=1
                    
            elif left[i]<right[j]:
                m.append(left[i])
                i+=1


            
    m.extend(left[i:])
    m.extend(right[j:])

    return m



anagram(["a", "b", "ab", "ba", "abc", "cba", "bac"])
