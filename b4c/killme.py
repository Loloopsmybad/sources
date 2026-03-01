maxsize  = 5 
top=-1 

def pop(stack):
    global top 
    if (stack==[]):
         print("\n Stack is UnderFlow \n")

    else: 
        n=stack[top] 
        stack.pop() 
        print("Removed Element ",n) 
        top=top-1

def push(stack): 
    global top 
    if (len(stack)==maxsize): 
        print("\n Stack is OverFlow \n ")

    else: 
        n=input("\nEnter an element to push :") 
        top=top+1 
        stack.append(n)

def traverse(stack): 
    if (stack==[]): 
        print("Stack is Empty")
    else:
        for i in stack: 
            print(i,end=" ")
def peak(stack): 
    global top 
    return stack[top]
def isFull(stack): 
    global maxsize 
    if (top==maxsize-1): 
        return True 
    else: 
        return False
    
def isEmpty(stack):
    if ( stack ==[]):
        return True 
    else: 
        return False
    

stack=[]
a=True
while a:
    print("\n1. Stack Push Operation ")
    print("2. Stack Pop Operation ")
    print("3. Show Peak / Top Position ")
    print("4. Traverse / Show Stack")
    print("5. Exit ")
    ch=int(input("Enter Choice :"))
    if ch == 1:
       push(stack)
    elif ch == 2:
        pop(stack)
    elif ch == 3:
        print("\n Peak Position ",peak(stack))
        print('Top is', top)
    elif ch == 4:
        traverse(stack)
    elif ch == 5:
        a=False
    else:
        print('Please enter a valid choice')
