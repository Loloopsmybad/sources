"""
def cube():
    x =  int(input("number:"))
    y = x**3
    return y
def test():
    assert cube() == 8
    assert cube()== -27
    assert cube() == 0
test()
print(cube())
"""

'''def is_positive(n):

    if n>0:
        return True
    elif n<0:
        return False
def test():
    assert is_positive(2)
    assert is_positive(-2)==False
n = int(input("no:"))

test()

if is_positive(n):
    print("True")
else:
    print("False")
'''
'''
def sum_list(n):
    x=0
    x=(n*(n+1))/2
    return x
def test():
    assert sum_list(2)==3
    assert sum_list(3)==6
x = int(input("num:"))
test()
sum_list(x)

'''

def iot(x):
        a=str(x)
        p=""
        for i in range (len(a)):
            for j in range (len(a)-1,-1,-1):
                
                if a[i]==a[j] :
                    p=p+a[j]

        print(p)
        print(a)
        if p== a:
            return "True"
        else:
            return "False"
        
print(iot(121))