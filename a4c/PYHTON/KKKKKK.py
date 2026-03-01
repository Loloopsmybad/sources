 
def POWER(X,Y):
    X**Y
    print(X**Y)
def ADITTION(X,Y):
     X+Y
     print(X+Y)

NUM_X = int(input('NUMBER 1-->'))
NUM_Y = int(input('NUMBER 2-->'))
OPERATOR_OP = input('what is your operator +,-,/,*,^ --> ')
if OPERATOR_OP == '^' :

 POWER(NUM_X,NUM_Y)

if OPERATOR_OP == '+' :

 ADITTION(NUM_X,NUM_Y)


