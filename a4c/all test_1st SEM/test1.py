nu=[-5, -5, -4, 0, 0, 3, 3, 4, 5]
countz=0
class Solution(object):
    def threeSumClosest(self, nums, target):
        nu=nums
        nu.sort()
        countz=0
        if len(nu)>3:

         for i in range(0,len(nu)-1):
           
            if nu [i] == 0:
                countz+=1
                if countz >= 1 :
                    nu.remove(0)
        
        print(nu)
        a=[]
        c=0
        d=0
        for i in range (len(nu)):
                if i+2 <= (len(nu)-1) and len(nu)>2 : 
                    if (nu[i] + nu[(i+1)] + nu[(i+2)]==target) or (nu[i] + nu[(i+1)] + nu[(i+2)]>=target) or (nu[i] + nu[(i+1)] + nu[(i+2)]<=target)  :
                        a.append(nu[i] + nu[(i+1)] + nu[(i+2)])
                        print (a)
                elif i+1 <= (len(nu)-1) and len(nu)==2 : 
                    if (nu[i] + nu[(i+1)]==target) or (nu[i] + nu[(i+1)] >=target) or (nu[i] + nu[(i+1)] <=target)  :
                        a.append(nu[i] + nu[(i+1)] )
                        print (a)
                elif len(nu)==1:
                    a.append(nu[i])

                
        for i in range (len(a)):
            if c ==0 and len(a)!=1:
                c=abs(target-a[i])
                d=a[i]
            elif abs(target-a[i]) <= c:
                c=a[i]
                d=a[i]
            elif len(a)==1:
                d =a[i]1
        print (d)

                
        return d
print(nu)